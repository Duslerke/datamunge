from io import TextIOWrapper
import pandas as pd
import re
from functools import reduce

target_odf_path = "data/input/file_name.ods"

odf_file = pd.ExcelFile(target_odf_path, engine="odf")

year_sheet_names = [name for name in odf_file.sheet_names if name.isdigit()]

print(year_sheet_names)


def clean_column_name(column_name: str) -> str:
    trimmed_name = column_name.strip()
    no_excessive_ws = re.sub('\\s+', ' ', trimmed_name)
    removed_symbols = re.sub('[?.]', '', no_excessive_ws)
    dash_to_space = removed_symbols.replace('-', ' ')
    lower_case = dash_to_space.lower()
    return lower_case


def extract_sheet_cols_as_set(path_to_file: str, sheet_name: str) -> set[str]:
    data_frame = pd.read_excel(path_to_file, engine="odf", sheet_name=sheet_name)
    columns_list = [clean_column_name(column_name) for column_name in data_frame.columns]
    return set(columns_list)


def join_write(file: TextIOWrapper, input_set: set[str], prefix: str = '', separator: str = ', ') -> None:
    print(f'diff cols count: {len(input_set)}')
    joined_col_names = separator.join(input_set)
    sheet_cols_line = prefix + separator + joined_col_names + '\n'
    file.write(sheet_cols_line)


def write_rows_to_csv(rows: list[set[str]], file_name: str) -> None:
    csv_file = open(f"data/output/{file_name}.csv", "w")
    for row in rows:
        join_write(csv_file, row)
    csv_file.close()

# Create a list of cleaned up column names for each sheet tab. Write as separate rows to a CSV.
col_sets_by_sheet = [extract_sheet_cols_as_set(target_odf_path, name) for name in year_sheet_names]
write_rows_to_csv(col_sets_by_sheet, "plant_diversity/col_names")

# # check col match between 1st 4 years
# cols_132=col_sets_by_sheet[:4]
# union_col_names_132 = sorted(reduce(lambda a, b: a.union(b), cols_132))
# print(len(union_col_names_132))

# Get the cleaned up, sorted, deduplicated list of unique column names across all of the sheet tabs.
union_col_names = sorted(reduce(lambda a, b: a.union(b), col_sets_by_sheet))
# print(len(union_col_names))
write_rows_to_csv([union_col_names], "plant_diversity/union_col_names")

# Find the column differences between the following 'year' sheet tabs (Year Sheets).
s2002 = col_sets_by_sheet[1]
s2015 = col_sets_by_sheet[4]
s2024 = col_sets_by_sheet[5]

d15m2 = sorted(s2015.difference(s2002))
d24m2 = sorted(s2024.difference(s2002))
d24m15 = sorted(s2024.difference(s2015))

text_file = open("data/output/plant_diversity/diff_cols.csv", "w")

join_write(text_file, d15m2, '2015-2002:')
join_write(text_file, d24m2, '2024-2002:')
join_write(text_file, d24m15, '2024-2015:')

text_file.close()

odf_file.close()

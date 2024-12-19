from typing import Iterable
import pandas as pd
from functools import reduce
from pathlib import Path

def get_unique_sheet_columns(data_frame: pd.DataFrame) -> set[str]:
    columns_list = data_frame.columns
    return set(columns_list)

def read_sheet(file: pd.ExcelFile, sheet_name: str) -> pd.DataFrame:
    return file.parse(sheet_name)

def add_missing_columns_to_df(incomplete_df: pd.DataFrame, full_column_names_set: Iterable[str], sheet_name: str) -> pd.DataFrame:
    # Adds missing columns to the given sheet tab data frame.
    df_union_cols = incomplete_df.reindex(columns=full_column_names_set, fill_value=None)
    # Add year column to df - needed within each row for data analysis steps using 'R'.
    df_union_cols.insert(loc=0, column='Year', value=sheet_name)
    return df_union_cols

def write_rows_to_csv(data_frame: pd.DataFrame, file_name: str) -> None:
        filepath = Path(f"data/output/{file_name}.csv")
        filepath.parent.mkdir(parents=True, exist_ok=True)
        data_frame.to_csv(filepath)

rel_file_path="data/input/plant_diversity/DIversity.ods"

# Open the plant diversity ODS file with multiple sheet tabs.
with pd.ExcelFile(rel_file_path, engine="odf") as odf_file:
    # Extract sheet tabs where same kind of data was collected yearly.
    year_sheet_names = [name for name in odf_file.sheet_names if name.isdigit()]
    sheet_tabs = { sheet_name: read_sheet(odf_file, sheet_name) for sheet_name in year_sheet_names }
    # print([*sheet_tabs])

    # Extract column names from each 'year' sheet tab, and union them together to get a Unique list of columns across all sheet tabs.
    sheet_dataframes = list(sheet_tabs.values())
    column_name_sets_by_sheet = [get_unique_sheet_columns(sheet_df) for sheet_df in sheet_dataframes]
    unique_column_names_across_sheets = reduce(lambda a, b: a.union(b), column_name_sets_by_sheet)

    # re-order combined columns
    # Sheet tab named '2002' has columns schema that is the most common out of all sheet tabs, as such it was arbitrarily chosen as a reference point.
    # This is done so the most common column order is preserved. Column names not present within this reference are appended to become last columns.
    ordered_column_names_2002 = list(sheet_tabs['2002'].columns)
    newCols = unique_column_names_across_sheets.difference(set(ordered_column_names_2002))
    semi_ordered_cols_list = ordered_column_names_2002 + list(newCols)

    # Make it so each 'year' sheet tab gains the column names it is missing so that the column set across all tabs is the same.
    df_sheets_with_all_columns = {
        sheet_name: add_missing_columns_to_df(sheet_df, semi_ordered_cols_list, sheet_name)
        for (sheet_name, sheet_df)
        in sheet_tabs.items()
    }

    # No longer needed, but keeping this as a reference:
    # Filter N/As
    # df_sheets_with_all_columns.replace({'\s*N/A\s*': None}, regex=True, inplace=True)

    # Combine all 'year' sheet tabs that have been column-corrected.
    combined_sheet_df = pd.concat(df_sheets_with_all_columns, ignore_index=True)

    write_rows_to_csv(combined_sheet_df, file_name="plant_diversity/combined_sheets")

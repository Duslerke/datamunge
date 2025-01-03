import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
})

df2 = pd.DataFrame({
    'c': [10, 11],
    'd': [12, 13],
    'e': [14, 15],
    'f': [16, 17]
})

# List of all desired columns
all_columns = list(set(['a','c', 'b', 'd', 'e', 'f']))

# Reindex the DataFrames to have the same columns and fill missing columns with None
df1_reindexed = df1.reindex(columns=all_columns, fill_value=None)
df2_reindexed = df2.reindex(columns=all_columns, fill_value=None)

# Concatenate the DataFrames
combined_df = pd.concat([df1_reindexed, df2_reindexed], ignore_index=True)

combined_df.insert(loc=0, column='Year', value='2022')

print(combined_df)

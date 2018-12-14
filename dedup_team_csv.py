import pandas as pd
import csv

file_name = "team_dedup.csv"
file_name_output = "team_dedup_processed.csv"

df = pd.read_csv(file_name, sep="\t or ,", engine="python")

# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  
df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
df.to_csv(file_name_output)
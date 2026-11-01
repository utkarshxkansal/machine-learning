import pandas as pd
df = pd.read_json("Reading of data/sample_Data.json")
print("reading first 10 rows:")
print(df.head(10))
print("reading last 10 rows:")
print(df.tail(10))
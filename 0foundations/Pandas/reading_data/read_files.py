import pandas as pd
#reading a file
df = pd.read_csv("Reading of data/customers-2000000.csv")
print(df)
dj = pd.read_json("Reading of data/sample_Data.json")
print(dj)
dxl = pd.read_excel("Reading of data/SampleSuperstore.xlsx")
print(dxl)

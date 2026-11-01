import pandas as pd
data = {
    "name": ["John", "Jane", "Doe"],
    "age": [2, 34, 290],
    "city": ["New York", "Los Angeles", "Chicago"],
    "salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')
print(f'dtypes: {df.dtypes}')
import pandas as pd
data = {
    "name": ["John", "Jane", "Doe"],
    "age": [2, 34, 290],
    "city": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
print(df.describe())

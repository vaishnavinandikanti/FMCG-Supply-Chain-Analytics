import pandas as pd

print("Loading data...")
# The DataCo dataset has some special characters, so we use 'latin-1' encoding to read it properly.
file_path = 'DataCoSupplyChainDataset.csv'
df = pd.read_csv(file_path, encoding='latin-1')

print("\n=== 1. Shape of the Dataset (Rows, Columns) ===")
print(df.shape)

print("\n=== 2. Column Names & Data Types ===")
# This tells us which columns are numbers, which are text, and which need date conversion.
print(df.dtypes)

print("\n=== 3. Missing Values (Columns with NULLs) ===")
# We only want to see columns that actually have missing data.
missing = df.isnull().sum()
print(missing[missing > 0])

print("\n=== 4. Duplicate Rows ===")
print(f"Number of exact duplicate rows: {df.duplicated().sum()}")

print("\n=== 5. First 3 Rows of Data ===")
print(df.head(3))
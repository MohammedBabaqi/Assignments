import pandas as pd
import numpy as np

data = {
    "Transaction_ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Customer_Name": ["Ahmed Ali", "Sara Omar", "Ali Saleh", "Nada Hassan", "Omar Khalid", "Ahmed Ali"],
    "Age": [28, np.nan, 35, 42, np.nan, 28],
    "Email": ["ahmed@mail.com", "sara@mail.com", np.nan, "nada@mail.com", "omar@mail.com", "ahmed@mail.com"],
    "Join_Date": ["2025-01-10", "2025-02-15", "2025-03-20", np.nan, "2025-05-05", "2025-01-10"],
    "Total_Purchase": [250, 300, 150, 400, np.nan, 250]
}

df = pd.DataFrame(data)

df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce") 

rows_missing_multiple = df[df.isnull().sum(axis=1) > 1]

info = df.info()
shape = df.shape

missing_per_column = df.isnull().sum()

under_30 = df[df["Age"] < 30]

df_no_missing = df.dropna()
remaining_rows = len(df_no_missing)

df["Age"].fillna(df["Age"].mean(), inplace=True)

df["Total_Purchase"].fillna(0, inplace=True)

duplicates = df[df.duplicated()]
df_cleaned = df.drop_duplicates()

print("1- Rows with more than one missing value:\n", rows_missing_multiple, "\n")
print("2- Missing values per column:\n", missing_per_column, "\n")
print("3- Customers under 30:\n", under_30, "\n")
print("4- Remaining rows after dropping missing values:", remaining_rows, "\n")
print("5- Duplicate rows before removal:\n", duplicates, "\n")
print("6- Final cleaned DataFrame:\n", df_cleaned)

# Clean_data.py
import pandas as pd
from sklearn.impute import (
    SimpleImputer,
)  # Importing SimpleImputer for handling missing values

# Load the data
df = pd.read_csv("../data/employee_data.csv")
print("Data loaded successfully with shape:", df.shape)

# Fix missing values
imputer = SimpleImputer(strategy="median")
df["salary"] = imputer.fit_transform(df[["salary"]])

# create enagement trend ( average of last 3 months)
df["engagement_trend"] = df[["engagement_score"]].rolling(window=3).mean()
df["engagement_trend"] = df["engagement_trend"].shift(1)  # Shift to avoid data leakage

# Save cleaned data to csv
df.to_csv("../data/cleaned_employee_data.csv", index=False)
print("Cleaned data saved successfully with shape:", df.shape)

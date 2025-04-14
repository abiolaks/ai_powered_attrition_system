import pandas as pd
import numpy as np
from faker import Faker


# Set seed for reproducibility
np.random.seed(42)
fake = Faker()
Faker.seed(42)

# Department configuration
departments = [
    "TSS",
    "Datazone",
    "Finance",
    "HR",
    "PMO",
    "Sales",
    "GRCS",
    "Customer Success",
    "Marketing and Communications",
    "Business Solution",
    "Product Engineering",
]
department_weights = [0.08, 0.07, 0.09, 0.06, 0.05, 0.15, 0.07, 0.1, 0.08, 0.1, 0.15]

# Base salary configuration (mean salaries by department)
department_salaries = {
    "TSS": 65000,
    "Datazone": 82000,
    "Finance": 68000,
    "HR": 58000,
    "PMO": 72000,
    "Sales": 75000,
    "GRCS": 69000,
    "Customer Success": 63000,
    "Marketing and Communications": 67000,
    "Business Solution": 78000,
    "Product Engineering": 95000,
}

# Generate synthetic data
data = {
    "employee_id": [f"E{str(i).zfill(4)}" for i in range(1000)],
    "department": np.random.choice(departments, size=1000, p=department_weights),
    "salary": np.zeros(1000),
    "tenure": np.clip(np.random.gamma(3, 1, 1000).round(1), 0, 10),  # 0-10 years
    "engagement_score": np.random.beta(2, 2, 1000) * 4 + 1,  # 1-5 scale
    "attrition": np.zeros(1000),
    "last_promotion_date": [
        fake.date_between(start_date="-5y", end_date="today") for _ in range(1000)
    ],
    "working_hours_per_month": np.clip(np.random.normal(160, 20, 1000), 120, 200).round(
        1
    ),
    "kpi_score": np.clip(np.random.beta(2, 5, 1000) * 100, 0, 100).round(1),
    "work_life_balance_score": np.random.choice(
        [1, 2, 3, 4, 5], size=1000, p=[0.1, 0.2, 0.4, 0.2, 0.1]
    ),
    "overtime_hours": np.random.poisson(5, 1000),
    "job_satisfaction": np.random.choice(
        [1, 2, 3, 4, 5], size=1000, p=[0.05, 0.15, 0.4, 0.3, 0.1]
    ),
    "number_of_projects": np.random.poisson(3, 1000),
    "distance_from_home": np.random.randint(1, 50, 1000),
    "trainings_and_certifications": np.random.poisson(3, 1000),
    "hire_date": [
        fake.date_between(start_date="-10y", end_date="-6m") for _ in range(1000)
    ],
}

# Create DataFrame
df = pd.DataFrame(data)


# Add department-based salary variations
for dept in departments:
    mask = df["department"] == dept
    size = sum(mask)
    df.loc[mask, "salary"] = np.random.normal(
        loc=department_salaries[dept],
        scale=department_salaries[dept] * 0.15,  # 15% standard deviation
        size=size,
    ).round(2)

# Add realistic attrition patterns (20% attrition rate)
df["attrition"] = np.random.choice([0, 1], size=1000, p=[0.8, 0.2])
df

# Add correlations for attrition
df.loc[df["attrition"] == 1, "engagement_score"] *= 0.8  # 20% lower engagement
df.loc[df["attrition"] == 1, "tenure"] *= 0.7  # 30% shorter tenure
df.loc[df["attrition"] == 1, "work_life_balance_score"] = np.random.choice(
    [1, 2, 3], size=sum(df["attrition"]), p=[0.3, 0.5, 0.2]
)
df.loc[df["attrition"] == 1, "overtime_hours"] += 2  # Higher overtime for attriters

# Add missing data (5% missing in engagement_score, 2% in salary)
df.loc[
    np.random.choice([True, False], size=1000, p=[0.05, 0.95]), "engagement_score"
] = np.nan
df.loc[np.random.choice([True, False], size=1000, p=[0.02, 0.98]), "salary"] = np.nan

# Convert dates
df["last_promotion_date"] = pd.to_datetime(df["last_promotion_date"])
df["hire_date"] = pd.to_datetime(df["hire_date"])

# Final data cleanup
df = df.round({"engagement_score": 2, "kpi_score": 1})
df = df[
    [
        "employee_id",
        "department",
        "salary",
        "tenure",
        "engagement_score",
        "attrition",
        "last_promotion_date",
        "working_hours_per_month",
        "kpi_score",
        "work_life_balance_score",
        "overtime_hours",
        "job_satisfaction",
        "number_of_projects",
        "distance_from_home",
        "trainings_and_certifications",
        "hire_date",
    ]
]
df.type

# Save to CSV
df.to_csv("employee_data_v2.csv", index=False)
print("Synthetic data generated with shape:", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))

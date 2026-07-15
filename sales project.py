import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET
df = pd.read_excel(
    r"C:\Users\gneer\Downloads\Sample_Superstore_Dataset.xlsx"
)

# DISPLAY DATASET
print("FIRST 5 ROWS")
print(df.head())

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET SHAPE")
print(df.shape)

# CHECK MISSING VALUES
print("\nMISSING VALUES")
print(df.isnull().sum())

# HANDLE MISSING VALUES
df["Customer Name"] = df["Customer Name"].fillna("Unknown")

if "Postal Code" in df.columns:
    df["Postal Code"] = df["Postal Code"].fillna(
        df["Postal Code"].median()
    )

# REMOVE DUPLICATES
print("\nROWS BEFORE:", len(df))

df = df.drop_duplicates()

print("ROWS AFTER:", len(df))

# CONVERT DATE COLUMNS
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    errors="coerce"
)

# CREATE SHIPPING DAYS COLUMN
df["Shipping Days"] = (
    df["Ship Date"] -
    df["Order Date"]
).dt.days

# SAVE CLEANED DATASET
df.to_excel(
    "Cleaned_Superstore.xlsx",
    index=False
)

# CREATE SUMMARY REPORT
summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Unique Customers",
        "Total Quantity Sold",
        "Average Shipping Days"
    ],
    "Value": [
        round(df["Sales"].sum(), 2),
        round(df["Profit"].sum(), 2),
        df["Order ID"].nunique(),
        df["Customer ID"].nunique(),
        df["Quantity"].sum(),
        round(df["Shipping Days"].mean(), 2)
    ]
})

print("\nSUMMARY REPORT")
print(summary)

summary.to_excel(
    "Summary_Report.xlsx",
    index=False
)

# SALES BY REGION
region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Region_Sales.png")
plt.show()

# PROFIT BY CATEGORY
category_profit = (
    df.groupby("Category")["Profit"]
      .sum()
)

plt.figure(figsize=(7, 7))
category_profit.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Profit by Category")
plt.ylabel("")
plt.savefig("Profit_by_Category.png")
plt.show()

# SALES BY SEGMENT
segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
)

plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")
plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Segment_Sales.png")
plt.show()

# TOP 10 PRODUCTS
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12, 6))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Top_10_Products.png")
plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY")

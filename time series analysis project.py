import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_excel(
    r"C:\Users\gneer\Downloads\Retail_Sales_Practice.xlsx"
)

# Fix dates
df['Date'] = pd.to_datetime(
    df['Date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)

# Fill missing Units Sold
df['Units Sold'] = df['Units Sold'].fillna(
    df['Units Sold'].median()
)

# Calculate Revenue
df['Total Revenue (₹)'] = (
    df['Units Sold']
    * df['Unit Price (₹)']
    * (1 - df['Discount (%)'] / 100)
)

# Sort by Date
df = df.sort_values('Date')

# Create Days column
df['Days'] = (
    df['Date']
    - df['Date'].min()
).dt.days

# Features and target
X = df[['Days']]
y = df['Total Revenue (₹)']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predictions on existing data
pred_train = model.predict(X)

# Accuracy
mae = mean_absolute_error(y, pred_train)

print("Mean Absolute Error:", round(mae, 2))

# Forecast next 30 days
future_days = pd.DataFrame({
    'Days': range(
        df['Days'].max() + 1,
        df['Days'].max() + 31
    )
})

predictions = model.predict(future_days)

# Forecast table
forecast = pd.DataFrame({
    'Future Day': future_days['Days'],
    'Predicted Revenue': predictions
})

print(forecast.head())

# Save output
forecast.to_excel(
    "Sales_Forecast_Output.xlsx",
    index=False
)

# Visualization
plt.figure(figsize=(10,6))

plt.scatter(
    df['Days'],
    df['Total Revenue (₹)'],
    label='Actual Revenue'
)

plt.plot(
    future_days['Days'],
    predictions,
    label='Forecast'
)

plt.xlabel("Days")
plt.ylabel("Revenue (₹)")
plt.title("Revenue Forecasting")

plt.legend()

plt.show()

print("Project Completed Successfully")

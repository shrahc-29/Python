import pandas as pd

# Sample data with outliers
sales_data = pd.DataFrame({
    'monthly_sales': [120, 130, 125, 128, 2000, 135, 140, 115, 118, 3000]
})

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = sales_data['monthly_sales'].quantile(0.25)
Q3 = sales_data['monthly_sales'].quantile(0.75)

# Calculate Interquartile Range (IQR)
iqr_value = Q3 - Q1

# Define lower and upper bounds
lower_limit = Q1 - 1.5 * iqr_value
upper_limit = Q3 + 1.5 * iqr_value

# Filter data to remove outliers
cleaned_sales_data = sales_data[
    (sales_data['monthly_sales'] >= lower_limit) &
    (sales_data['monthly_sales'] <= upper_limit)
]

print("Original data:")
print(sales_data)

print("\nData after removing outliers:")
print(cleaned_sales_data)

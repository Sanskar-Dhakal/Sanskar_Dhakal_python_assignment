

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Load the data
df = pd.read_csv('/home/sanskar/Downloads/python/Sanskar_Dhakal_python_assignment/week_4/vcs/bhatbhateni_sales.csv')
print(df.head())
print(df.columns)

df.shape

print(df.dtypes)

print(df.describe)

print(df.isna().sum())

print(df.isnull().sum() / len(df) * 100)       # percent missing per column

print("Duplicate rows:", df.duplicated().sum())

# Step 6: Remove duplicate rows
print("Before:", df.shape[0])
df = df.drop_duplicates()
print("After:", df.shape[0])

df['CustomerName'] = df['CustomerName'].fillna('Unknown Customer')

most_common_category = df['ProductCategory'].mode()[0]

print(most_common_category)

df['ProductCategory'] = df['ProductCategory'].fillna(most_common_category)

price_common=df['TotalAmount'] / df['Quantity']

df['UnitPrice'] = df['UnitPrice'].fillna(price_common)

df['PaymentMethod'] = df['PaymentMethod'].fillna('Unknown')

print(df.isnull().sum())

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()
print(df.head())

print(df['ProductCategory'].value_counts())
df['ProductCategory'].value_counts().plot(kind='bar')
plt.title('Transactions by Category')
plt.show()

print(df['Branch'].value_counts())

print(df['PaymentMethod'].value_counts())

monthly_sales = df.groupby('Month')['TotalAmount'].sum()
print(monthly_sales)
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Revenue')
plt.show()

# Revenue per day of week
day_sales = df.groupby('DayOfWeek')['TotalAmount'].sum()
print(day_sales)

# Total revenue per branch
branch_sales = df.groupby('Branch')['TotalAmount'].sum().sort_values(ascending=False)
print(branch_sales)





# Extract city from 'Branch' column
df['City'] = df['Branch'].apply(lambda x: x.split(' - ')[0])

city_sales = df.groupby('City')['TotalAmount'].sum().sort_values(ascending=False)
print(city_sales)

# Visualize sales by city
city_sales.plot(kind='bar')
plt.title('Total Revenue by City')
plt.xlabel('City')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

category_sales = df.groupby('ProductCategory')['TotalAmount'].sum().sort_values(ascending=False)
print(category_sales)

top_products_qty = df.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False).head(10)
print(top_products_qty)

top_products_rev = df.groupby('ProductName')['TotalAmount'].sum().sort_values(ascending=False).head(10)
print(top_products_rev)

top_customers = df.groupby('CustomerName')['TotalAmount'].sum().sort_values(ascending=False).head(10)
print(top_customers)

top_customers = df.groupby('CustomerName')['TotalAmount'].sum().sort_values(ascending=False).head(10)
print(top_customers)

# How many times each customer ordered
customer_order_counts = df.groupby('CustomerID')['TransactionID'].nunique()
repeat_customers = (customer_order_counts > 1).sum()
one_time_customers = (customer_order_counts == 1).sum()
print("Repeat customers:", repeat_customers)
print("One-time customers:", one_time_customers)

# Step 14: Payment method analysis

# Average transaction value per payment method
avg_by_payment = df.groupby('PaymentMethod')['TotalAmount'].mean()
print(avg_by_payment)

# Step 15: Correlation and outliers

# Correlation between number columns
print(df[['Quantity', 'UnitPrice', 'TotalAmount']].corr())

# Find outliers using IQR method
Q1 = df['TotalAmount'].quantile(0.25)
Q3 = df['TotalAmount'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df['TotalAmount'] < lower_limit) | (df['TotalAmount'] > upper_limit)]
print("Number of outliers:", len(outliers))


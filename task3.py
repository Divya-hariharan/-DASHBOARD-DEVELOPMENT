## Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')
%matplotlib inline
## Step 2: Load Dataset
df = pd.read_csv("sales_orders_dataset.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.head()
## Step 3: Total Revenue per Product
product_revenue = df.groupby('Product')['Total Revenue'].sum().sort_values(ascending=False)
sns.barplot(x=product_revenue.values, y=product_revenue.index, palette="viridis")
plt.title("Total Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()
## Step 4: Units Sold per Region
region_sales = df.groupby('Region')['Units Sold'].sum().sort_values()
sns.barplot(x=region_sales.values, y=region_sales.index, palette="coolwarm")
plt.title("Units Sold by Region")
plt.xlabel("Units Sold")
plt.ylabel("Region")
plt.show()
## Step 5: Monthly Revenue Trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Total Revenue'].sum()
monthly_revenue.plot(marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
## Step 6: Order Status Distribution
sns.countplot(x='Status', data=df, palette='pastel')
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")
plt.show()
## Step 7: Insights Summary

#- Laptops generated the highest revenue.
#- The North region had the most units sold.
#- Revenue varied across months, showing business activity trends.
#- Most orders were successfully completed, with few cancellations or pending statuses.

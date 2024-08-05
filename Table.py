import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the uploaded CSV file
file_path = 'Book1.csv'
data = pd.read_csv(file_path)

#1

# Pie chart: Distribution of order status
order_status_counts = data['OrderStatus'].value_counts()

plt.figure(figsize=(8, 8))
order_status_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'salmon'])
plt.title('Order Status Distribution')
plt.ylabel('')  # Hide the y-label
plt.show()

#2

# Convert the SaleDate column to datetime format
data['SaleDate'] = pd.to_datetime(data['SaleDate'], errors='coerce')

# Line chart: Change in total sales amount over time
daily_sales = data.groupby('SaleDate')['TotalAmount'].sum()

plt.figure(figsize=(12, 6))
daily_sales.plot(kind='line', marker='o', linestyle='-', color='b')
plt.title('Total Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.grid(True)
plt.show()

#3

# Bar chart: Compare total sales amount by payment method
payment_method_total = data.groupby('PaymentMethod')['TotalAmount'].sum()

plt.figure(figsize=(10, 6))
payment_method_total.plot(kind='bar', color='skyblue')
plt.title('Total Sales Amount by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Total Amount')
plt.grid(axis='y')
plt.show()

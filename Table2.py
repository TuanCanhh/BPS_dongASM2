import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'Book1.csv'
data = pd.read_csv(file_path)

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

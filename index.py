import pandas as pd

# Load the CSV file
file_path = 'Book1.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(data.head())

#1

# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)

#2

# Fill default values for missing columns
data['SaleID'].fillna( 1, inplace=True)
data['CustomerID'].fillna(2, inplace=True)
data['SaleDate'].fillna('23/01/2003', inplace=True)  # Default date
data['Quantity'].fillna(1, inplace=True)
data['TotalAmount'].fillna(0.0, inplace=True)
data['DiscountApplied'].fillna(0.0, inplace=True)
data['PaymentMethod'].fillna('Unknown', inplace=True)
data['ShippingAddress'].fillna('Unknown', inplace=True)
data['OrderStatus'].fillna('Unknown', inplace=True)

# Display data again after filling default values
print(data.head())

#3

# Convert date format
data['SaleDate'] = pd.to_datetime(data['SaleDate'], errors='coerce')

# Check data info after processing
print(data.info())

#4

# Save processed data to a new CSV file
output_file_path = 'Processed_Book12.csv'
data.to_csv(output_file_path, index=False)

print(output_file_path)


#5




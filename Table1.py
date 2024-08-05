import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
file_path = 'Book1.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Handle missing values by dropping rows with NaN values
data_cleaned = data.dropna(subset=['Quantity', 'TotalAmount'])

# Extract independent and dependent variables after cleaning
X_cleaned = data_cleaned[['Quantity']].values
Y_cleaned = data_cleaned['TotalAmount'].values

# Split the cleaned dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_cleaned, Y_cleaned, test_size=0.2, random_state=0)

# Create a linear regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, Y_train)

# Make predictions using the testing data
Y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X_test, Y_test, color='blue', label='Actual')
plt.plot(X_test, Y_pred, color='red', linewidth=2, label='Predicted')
plt.title('Linear Regression: Quantity vs Total Amount')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.legend()
plt.grid(True)
plt.show()

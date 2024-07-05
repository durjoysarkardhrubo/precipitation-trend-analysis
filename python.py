import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pymannkendall as mk

# Reading the Excel file
file_path = r"C:\Users\durjo\OneDrive\Desktop\New folder (12)\input.xlsx"
df = pd.read_excel(file_path)

# Checking the first few rows of the DataFrame
print(df.head())

# Assuming the actual data starts from the first row, including headers
df = pd.read_excel(file_path, header=4)  # Adjust the header row as needed

# Checking the column names
print(df.columns)

# Performing Mann-Kendall Test
mk_test_result = mk.original_test(df['FEB'])
print(mk_test_result)

# Performing Sen's Slope Estimation
def sen_slope(y):
    n = len(y)
    slopes = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            slopes.append((y[j] - y[i]) / (j - i))
    return np.median(slopes)

sen_slope_result = sen_slope(df['FEB'])
print(f"Sen's Slope: {sen_slope_result}")

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df['YEAR'], df['FEB'], marker='o', linestyle='-', label='Data')

# Linear regression line
slope, intercept, r_value, p_value, std_err = linregress(df['YEAR'], df['FEB'])
plt.plot(df['YEAR'], intercept + slope * df['YEAR'], 'b', label='Linear Fit', linewidth=1)

plt.xlabel('Year')
plt.ylabel('Precipitation')
plt.title('February Precipitation Trend')
plt.legend()
plt.grid(True)
plt.show()

# Load the Excel files you created earlier
import pandas as pd
employees = pd.read_excel("emp_data.xlsx")
sales = pd.read_excel("sales_data.xlsx")
inventory = pd.read_excel("inventory_data.xlsx")

print(employees.head())
print(sales.head())
print(inventory.head())

import pandas as pd
from tabulate import tabulate

# Load CSV file
df = pd.read_csv("employee_client_vendor.csv")   # replace with your file name

# Display as table
print(tabulate(df, headers='keys', tablefmt='psql'))

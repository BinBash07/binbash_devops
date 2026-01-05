import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root12345",   # replace with your root password
    database="rubinod"          # replace with your database name
)
cursor = conn.cursor()

# Load mapping CSV
mapping = pd.read_csv("employee_mapping.csv")

# Update employees table with client_id and vendor_id
for _, row in mapping.iterrows():
    cursor.execute(
        "UPDATE employees SET client_id = %s, vendor_id = %s WHERE emp_id = %s",
        (int(row['client_id']), int(row['vendor_id']), int(row['emp_id']))  # 👈 cast to int
    )

conn.commit()
cursor.close()
conn.close()

print("Employee mapping with client and vendor table updated successfully!")


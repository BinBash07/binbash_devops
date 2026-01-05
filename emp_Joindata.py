import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root12345",
    database="rubinod"
)
query = """
SELECT e.emp_name, e.emp_dept, c.client_name, v.vendor_name
FROM employees e
LEFT JOIN client c ON e.client_id = c.client_id
LEFT JOIN vendor v ON e.vendor_id = v.vendor_id;
"""
df = pd.read_sql(query, conn)
df.to_csv("employee_client_vendor.csv", index=False)

conn.close()
print("Exported to employee_client_vendor.csv")
n
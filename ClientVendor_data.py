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

# Import client.csv
clients = pd.read_csv("client.csv")
for _, row in clients.iterrows():
    cursor.execute(
        "INSERT INTO client (client_name, client_email, client_city, client_phone) VALUES (%s, %s, %s, %s)",
        (row['client_name'], row['client_email'], row['client_city'], row['client_phone'])
    )

# Import vendor.csv
vendors = pd.read_csv("vendor.csv")
for _, row in vendors.iterrows():
    cursor.execute(
        "INSERT INTO vendor (vendor_name, vendor_email, vendor_city, vendor_phone) VALUES (%s, %s, %s, %s)",
        (row['vendor_name'], row['vendor_email'], row['vendor_city'], row['vendor_phone'])
    )

conn.commit()
cursor.close()
conn.close()

print("Client and Vendor data imported successfully!")

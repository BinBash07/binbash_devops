import pandas as pd
inventory = {
    "ItemID": [201, 202, 203, 204],
    "ItemName": ["Laptop", "Printer", "Desk Chair", "Monitor"],
    "Stock": [25, 40, 60, 30],
    "UnitPrice": [800, 150, 120, 300],
    "Supplier": ["Dell", "HP", "Ikea", "Samsung"]
}

df_inventory = pd.DataFrame(inventory)
df_inventory.to_excel("inventory_data.xlsx", index=False)
print(df_inventory)

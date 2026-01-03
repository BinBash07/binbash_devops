import pandas as pd
sales = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [10000, 12000, 9000, 15000, 13000],
    "Expenses": [7000, 8000, 6500, 9000, 8500],
    "Profit": [3000, 4000, 2500, 6000, 4500]
}

df_sales = pd.DataFrame(sales)
df_sales.to_excel("sales_data.xlsx", index=False)
print(df_sales)

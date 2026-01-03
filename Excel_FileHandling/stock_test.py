import pandas as pd
import matplotlib.pyplot as plt

# Sample business data
sales = {"Month":["Jan","Feb","Mar","Apr"], "Revenue":[100,120,90,150]}
df = pd.DataFrame(sales)

# Quick summary
print(df.describe())

# Visualization
df.plot(x="Month", y="Revenue", kind="bar", title="Monthly Revenue")
plt.show()

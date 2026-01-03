import pandas as pd
import matplotlib.pyplot as plt

# Example employee data
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Department": ["HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 60000, 55000, 65000]
}

df = pd.DataFrame(data)
df.to_excel("employees.xlsx", index=False)
df2=pd.read_excel("employees.xlsx")
print(df2)

# Visualization
df.plot(x="Name", y="Salary", kind="bar", title="Employee Salary")
plt.show()
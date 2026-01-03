import pandas as pd
import matplotlib.pyplot as plt

empdata={
          "Name":["Binod","Ranjan","Anuj","Shivam","Golu","Kamlesh","Ankit"],
          "Department":["Business Analysis","Cyber Security","Coding","Coding2","PR","Testing","Mafia"],
          "Salary": [150000, 85000, 55000, 56000,57000,58000,75000], 
          "JoiningDate": ["2022-02-22", "2024-03-10", "2024-07-01",
          "2024-09-20","2024-10-20","2024-11-25","2025-12-12"]
        }
    
df=pd.DataFrame(empdata)
df.to_excel("emp_data.xlsx",index=False)
df2=pd.read_excel("emp_data.xlsx")
print(df2.head())
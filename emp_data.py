import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",       # or your server IP
    user="root",            # your MySQL username
    password="root12345",# your MySQL root password
    database="rubinod"       # replace with your database name
)

cursor = conn.cursor()

# Insert 25 rows
employees = [
    ("Amit Sharma", "amit.sharma@example.com", "IT", "Delhi", 60000, 5000, "Ravi Kumar"),
    ("Priya Verma", "priya.verma@example.com", "HR", "Mumbai", 45000, 3000, "Sneha Patel"),
    ("Rahul Singh", "rahul.singh@example.com", "Finance", "Bangalore", 70000, 6000, "Anil Mehta"),
    ("Neha Gupta", "neha.gupta@example.com", "Marketing", "Chennai", 52000, 4000, "Karan Joshi"),
    ("Vikram Rao", "vikram.rao@example.com", "Sales", "Hyderabad", 48000, 3500, "Meena Iyer"),
    ("Sonia Kapoor", "sonia.kapoor@example.com", "IT", "Pune", 65000, 5500, "Ravi Kumar"),
    ("Arjun Nair", "arjun.nair@example.com", "Finance", "Delhi", 72000, 6200, "Anil Mehta"),
    ("Meera Das", "meera.das@example.com", "HR", "Kolkata", 46000, 3200, "Sneha Patel"),
    ("Kunal Jain", "kunal.jain@example.com", "Marketing", "Mumbai", 53000, 4100, "Karan Joshi"),
    ("Ritika Malhotra", "ritika.malhotra@example.com", "Sales", "Delhi", 49000, 3600, "Meena Iyer"),
    ("Suresh Reddy", "suresh.reddy@example.com", "IT", "Hyderabad", 67000, 5700, "Ravi Kumar"),
    ("Ananya Roy", "ananya.roy@example.com", "Finance", "Chennai", 71000, 6100, "Anil Mehta"),
    ("Deepak Yadav", "deepak.yadav@example.com", "HR", "Delhi", 47000, 3300, "Sneha Patel"),
    ("Pooja Mishra", "pooja.mishra@example.com", "Marketing", "Bangalore", 54000, 4200, "Karan Joshi"),
    ("Rohan Kapoor", "rohan.kapoor@example.com", "Sales", "Pune", 50000, 3700, "Meena Iyer"),
    ("Shweta Iyer", "shweta.iyer@example.com", "IT", "Mumbai", 68000, 5800, "Ravi Kumar"),
    ("Manish Agarwal", "manish.agarwal@example.com", "Finance", "Kolkata", 73000, 6300, "Anil Mehta"),
    ("Sneha Kulkarni", "sneha.kulkarni@example.com", "HR", "Chennai", 48000, 3400, "Sneha Patel"),
    ("Aditya Desai", "aditya.desai@example.com", "Marketing", "Delhi", 55000, 4300, "Karan Joshi"),
    ("Komal Bhatia", "komal.bhatia@example.com", "Sales", "Hyderabad", 51000, 3800, "Meena Iyer"),
    ("Nikhil Saxena", "nikhil.saxena@example.com", "IT", "Bangalore", 69000, 5900, "Ravi Kumar"),
    ("Rashmi Menon", "rashmi.menon@example.com", "Finance", "Mumbai", 74000, 6400, "Anil Mehta"),
    ("Ajay Khanna", "ajay.khanna@example.com", "HR", "Delhi", 49000, 3500, "Sneha Patel"),
    ("Divya Joshi", "divya.joshi@example.com", "Marketing", "Pune", 56000, 4400, "Karan Joshi"),
    ("Varun Malhotra", "varun.malhotra@example.com", "Sales", "Kolkata", 52000, 3900, "Meena Iyer")
]

sql = """
INSERT INTO employees (emp_name, emp_email, emp_dept, emp_city, emp_salary, emp_bonus, emp_manager)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(sql, employees)
conn.commit()

print(f"{cursor.rowcount} rows inserted.")

cursor.close()
conn.close()

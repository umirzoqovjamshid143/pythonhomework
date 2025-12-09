import matplotlib 
import pandas  as pd
import  numpy as np
from matplotlib import pyplot as plt 


# Task-1

# 1
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# 2
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# 3
top_student = df1.loc[df1['Average'].idxmax()]
# 4
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
# 5
subject_means = df1[['Math', 'English', 'Science']].mean()
subject_means.plot(kind='bar', title="Fanlar bo‘yicha o‘rtacha baholar")

# task-2
# 1
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
# 2
avg_salary = df3.groupby('Department')['Salary'].mean()
# 3
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
# 4
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100


# task-3
# 1
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
# 2
income_by_product = df4.groupby('Product')['Total_Price'].sum()
print(income_by_product)
# 3
most_ordered = df4['Product'].value_counts().idxmax()
# 4
avg_quantity = df4['Quantity'].mean()
# 5
df4.groupby('Product')['Total_Price'].sum().plot(kind='pie', autopct='%1.1f%%', title="Mahsulotlar bo‘yicha sotuv ulushi")

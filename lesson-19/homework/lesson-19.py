**Homework Assignment 1: Analyzing Sales Data**

You are given a dataset containing sales data for an e-commerce website. The dataset (`task\sales_data.csv`) has the following columns:

- `Date`: Date of the sale.
- `Product`: Name of the product sold.
- `Category`: Category to which the product belongs.
- `Quantity`: Number of units sold.
- `Price`: Price per unit.

**Tasks:**

1. Group the data by the `Category` column and calculate the following aggregate statistics for each category:
   - Total quantity sold.
   - Average price per unit.
   - Maximum quantity sold in a single transaction.

import pandas as pd


category_stats = df.groupby('Category').agg
(
    total_quantity_sold=('Quantity', 'sum'),
    average_price_per_unit=('Price', 'mean'),
    max_quantity_in_transaction=('Quantity', 'max'))
print(category_stats)


2. Identify the top-selling product in each category based on the total quantity sold.

# Step 1: Group by Category and Product, sum the quantities
product_sales = df.groupby(['Category', 'Product']).agg(
    total_quantity_sold=('Quantity', 'sum')
).reset_index()

# Step 2: For each category, find the product with the max total quantity sold
top_selling = product_sales.loc[
    product_sales.groupby('Category')['total_quantity_sold'].idxmax()
]

# Step 3: Show the result
print(top_selling)


3. Find the date on which the highest total sales (quantity * price) occurred.

# Step 1: Calculate total sales per row
df['TotalSales'] = df['Quantity'] * df['Price']

# Step 2: Group by Date and sum total sales
daily_sales = df.groupby('Date')['TotalSales'].sum()

# Step 3: Find the date with the highest total sales
max_sales_date = daily_sales.idxmax()
max_sales_value = daily_sales.max()

print(f"Date with highest total sales: {max_sales_date} (Total Sales: ${max_sales_value:.2f})")



**Homework Assignment 2: Examining Customer Orders**

You have a dataset (`task\customer_orders.csv`) containing information about customer orders. The dataset has the following columns:

- `OrderID`: Unique identifier for each order.
- `CustomerID`: Unique identifier for each customer.
- `Product`: Name of the product ordered.
- `Quantity`: Number of units ordered.
- `Price`: Price per unit.

**Tasks:**

1. Group the data by `CustomerID` and filter out customers who have made less than 20 orders.


df = customer.groupby('CustomerID')['OrderID'].size()

katta = df[df >= 20].index

natija = customer[customer['CustomerID'].isin(katta)]

# Step 4: Show the result
print(natija)


2. Identify customers who have ordered products with an average price per unit greater than $120.

df = customer.groupby('CustomerID')['Price'].mean()

price1=df[df>120].index

natija1 = customer[customer['CustomerID'].isin(price1)]

print(natija1)


3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

# 1. Total quantity and total price per product
summary = customer.groupby('Product').apply(
    lambda x: pd.Series({
        'total_quantity': x['Quantity'].sum(),
        'total_price': (x['Quantity'] * x['Price']).sum()
    })
)

filtered_summary = summary[summary['total_quantity'] >= 5]

print(filtered_summary)




**Homework Assignment 3: Population Salary Analysis**

1. "task\population.db" sqlite database has `population` table.

import sqlite3
import pandas as pd

# Path to your SQLite database file
db_path = r'task\population.db'

# Connect to the database
conn = sqlite3.connect(db_path)

# Read the entire population table into a pandas DataFrame
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# Close the connection
conn.close()

# Show first few rows to confirm it loaded correctly
print(population_df.head())

2. "task\population salary analysis.xlsx" file defines Salary Band categories. <br />
    Read the data from population table and calculate following measures:
    - Percentage of population for each salary category;
    - Average salary in each salary category;
    - Median salary in each salary category;
    - Number of population in each salary category;

import sqlite3
import pandas as pd

# 1. Bazadan population jadvalini o‘qish
db_path = r'task\population.db'
conn = sqlite3.connect(db_path)
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# 2. Excel fayldan salary bandlarni o‘qish
excel_path = r'task\population salary analysis.xlsx'
salary_bands_df = pd.read_excel(excel_path)

# salary_bands_df taxminan quyidagi ustunlarga ega deb olamiz:
# 'Band' (kategoriya nomi), 'MinSalary' (minimum chegarasi), 'MaxSalary' (maksimum chegarasi)

# 3. Har bir ishchining maoshini mos salary bandga biriktirish uchun funksiya
def assign_salary_band(salary):
    for _, row in salary_bands_df.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Band']
    return 'Unknown'  # Agar mos kelmasa

population_df['SalaryBand'] = population_df['Salary'].apply(assign_salary_band)

# 4. Har bir salary band bo‘yicha hisoblashlar

# Aholi soni
count_per_band = population_df.groupby('SalaryBand').size()

# Umumiy aholi soni
total_population = len(population_df)

# Aholining foizi (percentage)
percentage_per_band = (count_per_band / total_population) * 100

# O‘rtacha maosh
average_salary_per_band = population_df.groupby('SalaryBand')['Salary'].mean()

# Median maosh
median_salary_per_band = population_df.groupby('SalaryBand')['Salary'].median()

# 5. Natijalarni bitta DataFrame-ga birlashtirish
salary_band_stats = pd.DataFrame({
    'Count': count_per_band,
    'Percentage': percentage_per_band,
    'AverageSalary': average_salary_per_band,
    'MedianSalary': median_salary_per_band
})

# 6. Natijani chiqarish
print(salary_band_stats)


3. Calculate the same measures in each State

# avvalgi kodni davom ettirib

# 1. Har bir State va SalaryBand bo‘yicha guruhlash va hisoblashlar
state_band_stats = population_df.groupby(['State', 'SalaryBand']).agg(
    Count=('Salary', 'count'),
    AverageSalary=('Salary', 'mean'),
    MedianSalary=('Salary', 'median')
).reset_index()

# 2. Har bir State uchun umumiy aholi sonini hisoblash
state_totals = population_df.groupby('State').size().reset_index(name='StateTotal')

# 3. state_band_stats ga shtat umumiy aholisini qo‘shish
state_band_stats = state_band_stats.merge(state_totals, on='State')

# 4. Foizni hisoblash (har bir salary band uchun shtatdagi foiz)
state_band_stats['Percentage'] = (state_band_stats['Count'] / state_band_stats['StateTotal']) * 100

# 5. Natijani ko‘rsatish
print(state_band_stats)




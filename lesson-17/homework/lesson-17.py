Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age

import pandas as pd

df = pd.DataFrame({
    'First Name': ['Ali', 'Vali'],
    'Age': [23, 31]
})

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print(df)


2. Print the first 3 rows of the DataFrame

df.head(3)
print(df.head(3))

3. Find the mean age of the individuals


means=df['age'].mean()

print(means)

4. Select and print only the 'Name' and 'City' columns

Namecity=df[['first_name','city']]

print(Namecity)


5. Add a new column 'Salary' with random salary values

import numpy as np

# 5000 dan 10000 gacha bo‘lgan tasodifiy ish haqi qiymatlarini qo‘shish
df['salary'] = np.random.randint(5000, 10001, size=len(df))

print(df)


6. Display summary statistics of the DataFrame

df.describe()
print(df.describe())


Homework 2:

1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data.
Use below table.

| Month | Sales | Expenses |
|-------|-------|----------|
| Jan   | 5000  | 3000     |
| Feb   | 6000  | 3500     |
| Mar   | 7500  | 4000     |
| Apr   | 8000  | 4500     |

new={'Month':['Jan','Feb','Mar','Apr'] ,'Sales':[5000,6000,7500,8000],
     'Expenses':[3000,3500,4000,4500]}
dfnew=pd.DataFrame(new)

print(dfnew=pd.DataFrame(new))

2. Calculate and display the maximum sales and expenses.

dfnew[['Sales','Expenses']].max()

dfnew[['Sales','Expenses']].max()

3. Calculate and display the minimum sales and expenses.

dfnew[['Sales','Expenses']].min()

print(dfnew[['Sales','Expenses']].min())

4. Calculate and display the average sales and expenses.

dfnew[['Sales','Expenses']].mean()

print(dfnew[['Sales','Expenses']].mean())

Homework 3:

1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

| Category       | January | February | March | April |
|----------------|---------|----------|-------|-------|
| Rent           | 1200    | 1300     | 1400  | 1500  |
| Utilities      | 200     | 220      | 240   | 250   |
| Groceries      | 300     | 320      | 330   | 350   |
| Entertainment  | 150     | 160      | 170   | 180   |

import pandas as pd

# Ma'lumotlar lug'at ko'rinishida
data1 = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data1)

# Natijani ko'rish
print(expenses)



2. Calculate and display the maximum expense for each category.
    
expenses.set_index('Category').max(axis=1)

3. Calculate and display the minimum expense for each category.

 expenses.set_index('Category').min(axis=1)   

4. Calculate and display the average expense for each category.

 expenses.set_index('Category').mean(axis=1)   



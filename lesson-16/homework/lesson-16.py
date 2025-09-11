# 1. Convert List to 1D Array

Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

Expected Output:

Original List: [12.23, 13.32, 100, 36.32]
One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

import numpy as np

lst = [12.23, 13.32, 100, 36.32]
print("Original List:", lst)

arr = np.array(lst)
print("One-dimensional NumPy array:", arr)



# 2. Create 3x3 Matrix (2?10)

Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

Expected Output:

[[ 2 3 4]
[ 5 6 7]
[ 8 9 10]]

import numpy as np

# 2 dan 10 gacha bo'lgan 3x3 matritsa yaratish
matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)



# 3. Null Vector (10) & Update Sixth Value

Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np

# Null vector yaratish
vec = np.zeros(10)
print(vec)

# Oltinchi qiymatini 11 ga o'zgartirish (Python indekslash 0 dan boshlanadi, ya'ni 6-chi element indeksi 5)
vec[6] = 11
print("\nUpdate sixth value to 11")
print(vec)



# 4. Array from 12 to 38

Write a NumPy program to create an array with values ranging from 12 to 38.

Expected Output:

[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np
arr=np.arange(12,38)
print(arr)




# 5. Convert Array to Float Type

Write a NumPy program to convert an array to a floating type.

Sample output:

Original array
[1, 2, 3, 4]

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Original array")
print(arr)

float_arr = arr.astype(float)
print("\nArray converted to float type:")
print(float_arr)




# 6. Celsius to Fahrenheit Conversion

Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

Sample Array [0, 12, 45.21, 34, 99.91]
[-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

Expected Output:

Values in Fahrenheit degrees:
[ 0. 12. 45.21 34. 99.91 32. ]

Values in Centigrade degrees:
[-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Centigrade degrees:
[-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Fahrenheit degrees:
[-0. 12. 45.21 34. 99.91 32. ]

import numpy as np

# Santigrad qiymatlari
celsius = np.array([0, 12, 45.21, 34, 99.91])
print("Values in Centigrade degrees:")
print(celsius)

# Santigraddan Fahrenheitga o'tkazish
fahrenheit = (9/5) * celsius + 32
print("\nValues in Fahrenheit degrees:")
print(fahrenheit)



# 7. Append Values to Array (Do self-tudy)

Write a NumPy program to append values to the end of an array.

Expected Output:

Original array:
[10, 20, 30]

After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]

import numpy as np

# Original array
arr = np.array([10, 20, 30])
print("Original array:")
print(arr)

# Yangi qiymatlar
values_to_append = [40, 50, 60, 70, 80, 90]

# Qiymatlarni qo‘shish
new_arr = np.append(arr, values_to_append)
print("\nAfter append values to the end of the array:")
print(new_arr)


# 8. Array Statistical Functions (Do self-tudy)

Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

import numpy as np

# 10 elementli tasodifiy array yaratish (0 dan 100 gacha bo'lgan butun sonlar)
arr = np.random.randint(0, 101, size=10)
print("Random array:", arr)

# Mean (o'rtacha qiymat)
mean_val = np.mean(arr)
print("Mean:", mean_val)

# Median (median qiymat)
median_val = np.median(arr)
print("Median:", median_val)

# Standard deviation (standart og'ish)
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)


# 9 Find min and max 

Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

# 10x10 o'lchamdagi tasodifiy butun sonlar (0 dan 100 gacha)
arr = np.random.randint(0, 101, size=(10, 10))
print("Random 10x10 array:\n", arr)

# Minimum qiymatni topish
min_val = np.min(arr)
print("\nMinimum value:", min_val)

# Maksimum qiymatni topish
max_val = np.max(arr)
print("Maximum value:", max_val)





# 10 

Create a 3x3x3 array with random values.

import numpy as np

# 3x3x3 o'lchamdagi tasodifiy butun sonlar (0 dan 100 gacha)
arr = np.random.randint(0, 101, size=(3, 3, 3))
print("Random 3x3x3 array:\n", arr)

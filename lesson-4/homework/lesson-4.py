1. Sort a Dictionary by Value
 Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict9 = {'a': 10, 'b': 30, 'c': 20, 'd': 40}

sorted_dict_asc = dict(sorted(my_dict9.items(), key=lambda x: x[1]))
print("O'sish tartibida:", sorted_dict_asc)


sorted_dict_desc = dict(sorted(my_dict9.items(), key=lambda x: x[1], reverse=True))
print("Kamayish tartibida:", sorted_dict_desc)


 2. Add a Key to a Dictionary
 Write a Python script to add a key to a dictionary.

 Sample Dictionary:

{0: 10, 1: 20}
Expected Result:

{0: 10, 1: 20, 2: 30}

dic1={0: 10, 1: 20}
dic2={2: 30}

dic={**dic1, **dic2}

print(dic)


3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionaries:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
Expected Result:

 {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}

print(result)


 4. Generate a Dictionary with Squares
 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

 Sample Dictionary (n =5 ):

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=5

my_dic7={x:x*x for x in range(1,n+1)}

print(my_dic7)

 5. Dictionary of Squares (1 to 15)
 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

 Expected Output:

 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
 Set Exercises

squaresdict={}
for num in range(1, 16):  
    squaresdict[num] = num ** 2  
print(squaresdict)






 1. Create a Set
 Write a Python program to create a set.

my_set1={1,3,2,4,5,6}
print(my_set1)

 2. Iterate Over a Set
 Write a Python program to iterate over sets.

fruit={'apple','watermelon','peach','banana','tomato'}
for fruits in fruit:
    print(fruits)


 3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.

my_set={'Mathematics','Physics','Chemistry','Biology','History'}

my_set.add('English')
print(my_set)



 4. Remove Item(s) from a Set
 Write a Python program to remove item(s) from a given set.

my_set2={'Mathematics', 'English','Physics','Chemistry','Biology','History'}

my_set2.discard('Biology')

print(my_set2)



 5. Remove an Item if Present in the Set
 Write a Python program to remove an item from a set if it is present in the se

my_set3 = {'Mathematics', 'English', 'Physics', 'Chemistry', 'Biology', 'History'}
my_set3.discard('History')
print(my_set3)




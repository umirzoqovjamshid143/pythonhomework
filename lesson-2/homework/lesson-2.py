
1. Age Calculator Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

ism = input('Ismingizni kiriting: ')
yil = int(input('Tug\'ilgan yilingizni kiriting: '))

import datetime
hozirgi_yil = datetime.datetime.now().year
yosh = hozirgi_yil - yil

print(f"{ism}, sizning yoshingiz: {yosh}")


2. Extract Car Names Extract car names from the following text: txt = 'LMaasleitbtui'
txt = 'LMaasleitbtui'

car1=txt[::2]
car2=txt[1::2]
print(car1,car2)

3. Extract Car Names Extract car names from the following text: 
txt = 'MsaatmiazD'
car3=txt[::-2]
car4=txt[::2]
print(car3,car4)
4. Extract Residence Area Extract the residence area from the following text: txt = "I'am John. I am from London"

txt = "I'am John. I am from London"
sozlar = txt.split() 

if "from" in sozlar:
    indeks = sozlar.index("from")
    yashash_joyi = sozlar[indeks + 1]
    print("Yashash joyi:", yashash_joyi)


5. Reverse String Write a Python program that takes a user input string and prints it in reverse order.

user_input = input("hello")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)


6. Count Vowels Write a Python program that counts the number of vowels in a given string.
text = input("Salom dunyo" )
vowels = "aeiouAEIOU"

count = 0
for char in text:
    if char in vowels:
        count += 1
print("Unli harflar soni:", count)
7. Find Maximum Value Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers = input("Sonlarni vergul bilan kiriting: ")  # masalan: 3,5,7,2,9
num_list = [int(num) for num in numbers.split(",")]

max_value = num_list[0]
for num in num_list:
    if num > max_value:
        max_value = num

print("Eng katta qiymat:", max_value)
8. Check Palindrome Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

soz = input("So‘z kiriting: ")

if soz == soz[::-1]:
    print("Bu so‘z palindroma.")
else:
    print("Bu so‘z palindroma emas.")


9. Extract Email Domain Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Email manzilini kiriting: ")

domain = email.split("@")[-1]

print("Email domeni:", domain)


10. Generate Random Password Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

length = int(input("Parol uzunligini kiriting: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("Yaratilgan parol:", password)















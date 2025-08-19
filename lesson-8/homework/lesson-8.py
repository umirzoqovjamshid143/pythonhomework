

Exception Handling Exercises

1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    num = float(input("Enter a number to divide 10 by: "))  # Get number from user
    result = 10 / num  # Perform division
    print(f"Result: {result}")  # Print result
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  # Handle zero division error

2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    name = input("Enter your name: ")  # Get user's name
    age = int(input("Enter your age: "))  # Get age as integer
    print(f"Hello {name}, so you are {age} years old")  # Print greeting
except ValueError:
    print("Error: Please enter a valid integer for age.")  # Handle invalid input

3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    file_name = input("Enter the file name: ")  # Get file name from user
    with open(file_name, 'r') as file:  # Open file in read mode
        text = file.read()  # Read file content
        print(text)  # Print content
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")  # Handle missing file error

4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    a = float(input("Enter first number: "))  # Get first number
    b = float(input("Enter second number: "))  # Get second number
    print("Sum:", a + b)  # Print sum of numbers
except ValueError:
    print("Error: Please enter valid numbers.")  # Handle invalid number input
except TypeError as e:
    print(f"TypeError: {e}")  # Handle type error


5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    with open('myfile.txt', 'w') as file:  # Open file in write mode
        file.write('hello')  # Write 'hello' to file
    print("File written successfully.")  # Confirm successful write
except PermissionError:
    print("Error: Permission denied to write to file.")  # Handle permission error
except Exception as e:
    print(f"Unexpected error: {e}")  # Handle other errors

   


6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

def operate_on_list(lst, index):
    try:
        result = lst[index] * 2  # Double the element at given index
        print(f"Element at index {index} doubled: {result}")  # Print result
    except IndexError:
        print(f"Error: Index {index} is out of range.")  # Handle invalid index
    return lst  # Return list

# Example usage for IndexError
my_list = [1, 2, 3]
operate_on_list(my_list, 1)  # Valid index
operate_on_list(my_list, 5)  # Invalid index

7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    number = float(input("Enter a number: "))  # Get number from user
    print(f"You entered: {number}")  # Print entered number
except KeyboardInterrupt:
    print("\nInput cancelled by user.")  # Handle input cancellation
except ValueError:
    print("Error: Please enter a valid number.")  # Handle invalid input

8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    numerator = float(input("Enter the numerator: "))  # Get numerator
    denominator = float(input("Enter the denominator: "))  # Get denominator
    result = numerator / denominator  # Perform division
    print(f"Result of division: {result}")  # Print result
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  # Handle zero division
except ValueError:
    print("Error: Please enter valid numbers.")  # Handle invalid input

9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    file_path = input("Enter the file path: ")  # Get file path from user
    with open(file_path, 'r', encoding='utf-8') as file:  # Open file with UTF-8
        content = file.read()  # Read file content
        print("File content:")  # Print content header
        print(content)  # Print content
except UnicodeDecodeError as e:
    print(f"Encoding error: {e}. Try another encoding (e.g., 'latin1').")  # Handle encoding error
except FileNotFoundError:
    print("Error: File not found. Check the path.")  # Handle missing file
except PermissionError:
    print("Error: Permission denied to access file.")  # Handle permission error
except Exception as e:
    print(f"Unexpected error: {e}")  # Handle other errors


10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    my_list = [1, 2, 3, 4, 5]  # Create a list
    print("Original list:", my_list)  # Print original list
    result = my_list.append_new(10)  # Try non-existent method (raises AttributeError)
    print("Modified list:", my_list)  # Print modified list
except AttributeError as e:
    print(f"Attribute error: {e}")  # Handle attribute error
    my_list.append(10)  # Use correct method to append
    print("Modified list (correct method):", my_list)  # Print updated list
except Exception as e:
    print(f"Unexpected error: {e}")  # Handle other errors


1.Write a Python program to read an entire text file.

def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = []
        for _ in range(n):
            line = file.readline()
            if not line:  # End of file reached before n lines
                break
            lines.append(line.rstrip('\n'))
    return lines

# Example usage
file_path = 'example.txt'
n = 5  # Number of lines to read

first_lines = read_first_n_lines(file_path, n)

print(f"First {n} lines of the file:")
for line in first_lines:
    print(line)

2.Write a Python program to read first n lines of a file.

def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            # Read first n lines using islice for efficiency
            from itertools import islice
            lines = list(islice(file, n))
            if not lines:
                print("File is empty or has fewer lines than requested.")
                return
            for i, line in enumerate(lines, 1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ValueError:
        print("Error: Please provide a valid number of lines")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
filename = "example.txt"  # Replace with your file name
try:
    n = int(input("Enter the number of lines to read: "))
    if n <= 0:
        print("Please enter a positive number of lines")
    else:
        read_first_n_lines(filename, n)
except ValueError:
    print("Error: Please enter a valid integer")


3.Write a Python program to append text to a file and display the text.

# Define the file path
file_path = 'example.txt'

# Text to append
text_to_append = "This is the new line being appended.\n"

# Append text to the file
with open(file_path, 'a') as file:
    file.write(text_to_append)

# Read and display the file content
with open(file_path, 'r') as file:
    content = file.read()

print("Current contents of the file:")
print(content)

4.Write a Python program to read last n lines of a file.

# Fayldan oxirgi n ta qatordan iborat matnni o‘qiydigan dastur

def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines[-n:]  # Get the last n lines

# Example usage
file_path = 'example.txt'
n = 5  # Change this to the number of lines you want

last_lines = read_last_n_lines(file_path, n)

print(f"Last {n} lines of the file:")
for line in last_lines:
    print(line, end='')  # Avoid adding extra newlines
Notes:

5.Write a Python program to read a file line by line and store it into a list.

# Faylni qatorma-qator o‘qib, har bir qatorni ro‘yxatga saqlovchi dastur

# Define the file path (change this to your actual file path)
file_path = 'example.txt'

# Initialize an empty list to store the lines
lines_list = []

# Read the file line by line and store each line in the list
with open(file_path, 'r') as file:
    for line in file:
        lines_list.append(line.rstrip('\n'))  # Remove trailing newline character

# Print the list of lines
print("Lines stored in the list:")
print(lines_list)

6.Write a Python program to read a file line by line and store it into a variable.

# Define the file path (you can change this to your desired file)
file_path = 'example.txt'

# Read the file line by line and store it in a variable
with open(file_path, 'r') as file:
    lines = file.readlines()

# Print the contents stored in the variable
print("File contents stored in the variable:")
for line in lines:
    print(line, end='')  # 'end' avoids adding extra newlines


7.Write a Python program to read a file line by line and store it into an array.

# Define the file path
file_path = 'example.txt'

# Initialize an empty list to store lines
lines_array = []

# Open and read the file line by line
with open(file_path, 'r') as file:
    for line in file:
        lines_array.append(line.rstrip('\n'))  # Remove newline characters

# Print the array
print("Lines stored in the array:")
print(lines_array)

8.Write a Python program to find the longest words.

def find_longest_words(file_path):
    longest_words = []
    max_length = 0

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_len = len(word)
                if word_len > max_length:
                    max_length = word_len
                    longest_words = [word]
                elif word_len == max_length:
                    longest_words.append(word)

    # Remove duplicates by converting to a set, then back to list
    longest_words = list(set(longest_words))
    return longest_words, max_length

# Example usage
file_path = 'example.txt'
longest_words, length = find_longest_words(file_path)

print(f"Longest word length: {length}")
print("Longest word(s):")
for w in longest_words:
    print(w)


9.Write a Python program to count the number of lines in a text file.

def count_lines(filename):
    # Faylni ochamiz va har bir qatordagi matnni o'qib ro'yxatga olamiz
    with open(filename, 'r') as file:
        lines = file.readlines()  # Barcha qatordagi matnlar ro'yxat ko'rinishida saqlanadi
        return len(lines)  # Ro'yxat uzunligi - qatordagi son

# Fayl nomini yozamiz
filename = 'example.txt'  # O'zingizning fayl nomingizni kiriting
print(f"Faylda {count_lines(filename)} ta qatorda matn bor.")

10.Write a Python program to count the frequency of words in a file.

def count_word_frequency(filename):
    word_freq = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()  # Qatorni kichik harflarga o‘tkazib, so‘zlarga bo‘lamiz
            for word in words:
                word = word.strip('.,!?;"\'()[]')  # So‘zlardan tinish belgilarini olib tashlaymiz
                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1  # So‘zning sonini oshiramiz

    return word_freq

filename = 'example.txt'
freq = count_word_frequency(filename)

for word, count in freq.items():
    print(f"'{word}': {count}")

11.Write a Python program to get the file size of a plain file.

import os

def get_file_size(filename):
    size = os.path.getsize(filename)  # Fayl hajmini baytlarda olamiz
    return size

filename = 'example.txt'
size = get_file_size(filename)
print(f"Fayl hajmi: {size} bayt")

12.Write a Python program to write a list to a file.

def write_list_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')  # Har bir elementni yangi qatordan yozamiz

my_list = ['olma', 'banan', 'nok', 'shaftoli']
write_list_to_file('output.txt', my_list)
print("Ro'yxat faylga yozildi.")

13.Write a Python program to copy the contents of a file to another file.

def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dst:
        for line in src:
            dst.write(line)  # Har bir qatordagi matnni yangi faylga yozamiz

source_file = 'source.txt'
destination_file = 'copy.txt'
copy_file(source_file, destination_file)
print(f"'{source_file}' faylining mazmuni '{destination_file}' ga nusxalandi.")


14.Write a Python program to combine each line from the first file with the corresponding line in the second file.

def combine_files_line_by_line(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        for line1, line2 in zip(f1, f2):  # Ikkala fayldan mos qatordagi satrlarni olamiz
            combined_line = line1.strip() + ' ' + line2.strip()  # Qatordagi matnlarni bo‘shliq bilan birlashtiramiz
            out.write(combined_line + '\n')  # Natijani yangi faylga yozamiz

file1 = 'file1.txt'
file2 = 'file2.txt'
output = 'combined.txt'

combine_files_line_by_line(file1, file2, output)
print(f"Qatorlar '{file1}' va '{file2}' dan olib, '{output}' ga birlashtirildi.")


15.Write a Python program to read a random line from a file.

import random

def read_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Barcha qatordagi matnlarni ro'yxatga olamiz
    random_line = random.choice(lines).strip()  # Tasodifiy qatorni tanlab, bosh va oxirgi bo'shliqlarni olib tashlaymiz
    return random_line

filename = 'example.txt'
line = read_random_line(filename)
print(f"Fayldan tasodifiy olingan qator: {line}")


16.Write a Python program to assess if a file is closed or not.

filename = 'example.txt'

file = open(filename, 'r')  # Faylni ochamiz
print(f"Fayl yopilganmi? {file.closed}")  # Fayl holatini chiqaramiz (False — ochiq, True — yopiq)

file.close()  # Faylni yopamiz
print(f"Fayl yopilganmi? {file.closed}")  # Yana holatini tekshiramiz (True bo‘lishi kerak)

17.Write a Python program to remove newline characters from a file.

def remove_newlines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            clean_line = line.replace('\n', '')  # Yangi qator belgilarini olib tashlaymiz
            outfile.write(clean_line)       # Tozalangan qatordagi matnni yozamiz

input_file = 'input.txt'
output_file = 'output.txt'

remove_newlines(input_file, output_file)
print(f"Yangi qator belgilaridan tozalangan matn '{output_file}' fayliga yozildi.")

18.Write a Python program that takes a text file as input and returns the number of words in a given text file.
Note: Some words can be separated by a comma with no space.

import re

def count_words_in_file(filename):
    word_count = 0
    with open(filename, 'r') as file:
        for line in file:
            # So‘zlarni vergul, bo‘sh joy yoki boshqa tinish belgilariga qarab ajratamiz
            words = re.split(r'[,\s]+', line.strip())
            # Bo‘sh elementlarni olib tashlaymiz va so‘zlar sonini qo‘shamiz
            words = [w for w in words if w]
            word_count += len(words)
    return word_count

filename = 'example.txt'
total_words = count_words_in_file(filename)
print(f"Faylda jami {total_words} ta so‘z bor.")



19.Write a Python program to extract characters from various text files and put them into a list.

def extract_chars_from_files(filenames):
    chars_list = []
    for filename in filenames:
        with open(filename, 'r') as file:
            content = file.read()  # Fayldagi barcha matnni o‘qiymiz
            chars_list.extend(list(content))  # Har bir belgini ro‘yxatga qo‘shamiz
    return chars_list

file_list = ['file1.txt', 'file2.txt', 'file3.txt']
characters = extract_chars_from_files(file_list)
print(f"Barcha fayllardan olingan belgilar soni: {len(characters)}")
print("Belgilar ro'yxati:", characters)


20.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string

def create_alphabet_files():
    for letter in string.ascii_uppercase:  # A dan Z gacha harflar
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"Bu fayl {letter} harfi uchun.\n")  # Faylga qisqa matn yozamiz

create_alphabet_files()
print("A dan Z gacha fayllar yaratildi.")



21.Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string

def write_alphabet_to_file(filename, letters_per_line):
    letters = string.ascii_lowercase  # kichik harflar a-z
    with open(filename, 'w') as file:
        for i in range(0, len(letters), letters_per_line):
            line = letters[i:i+letters_per_line]
            file.write(line + '\n')  # Har bir qatorda belgilangan harflar soni yoziladi

filename = 'alphabet.txt'
letters_per_line = 5  # Har qatorda nechta harf bo‘lishi kerak
write_alphabet_to_file(filename, letters_per_line)
print(f"{filename} fayliga har bir qatorda {letters_per_line} ta harf yozildi.")

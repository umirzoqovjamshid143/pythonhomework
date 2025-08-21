Homework:

1.Create your own virtual environment and install some python packages.

import os
import subprocess
import sys

# 1. Virtual muhit nomi
env_name = "myenv"

# 2. Virtual muhit yaratish
print(f"'{env_name}' nomli virtual muhit yaratilmoqda...")
try:
    subprocess.run([sys.executable, "-m", "venv", env_name], check=True)
except subprocess.CalledProcessError:
    print("Xato: Virtual muhit yaratishda muammo yuz berdi!")
    sys.exit(1)

# 3. Paketlar ro‘yxati
packages = ["requests", "numpy", "pandas"]

# 4. Pip yo‘liga to‘liq kirish
pip_path = os.path.join(env_name, "Scripts", "pip") if os.name == "nt" else os.path.join(env_name, "bin", "pip")

# 5. Paketlarni o‘rnatish
for package in packages:
    print(f"'{package}' paketi o‘rnatilmoqda...")
    try:
        subprocess.run([pip_path, "install", package], check=True)
    except subprocess.CalledProcessError:
        print(f"Xato: '{package}' paketini o‘rnatishda muammo yuz berdi!")
        sys.exit(1)

print("Hammasi muvaffaqiyatli bajarildi!")



2.Create custom modules.
Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

def add(a, b):
    """Ikki sonni qo‘shish"""
    return a + b

def subtract(a, b):
    """Ikki sonni ayirish"""
    return a - b

def multiply(a, b):
    """Ikki sonni ko‘paytirish"""
    return a * b

def divide(a, b):
    """Ikki sonni bo‘lish"""
    if b == 0:
        return "Bo‘lishda nolga bo‘lish mumkin emas"
    return a / b

def reverse_string(s):
    """Satrni teskari qilish"""
    return s[::-1]

def count_vowels(s):
    """Satr ichidagi unli harflar sonini hisoblash"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

import math_operations
import string_utils

# Matematik amallar
print("Qo‘shish:", math_operations.add(10, 5))  # 15
print("Ayirish:", math_operations.subtract(10, 5))  # 5
print("Ko‘paytirish:", math_operations.multiply(10, 5))  # 50
print("Bo‘lish:", math_operations.divide(10, 5))  # 2.0

# Satr funksiyalari
print("Teskari satr:", string_utils.reverse_string("Salom"))  # molaS
print("Unlilar soni:", string_utils.count_vowels("Assalomu alaykum"))  # 6







3.Create custom packages.
Create geometry package.

 geometry\
     __init__.py
     circle.py
 
Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
Create file_operations package.
 file_operations\
     __init__.py
     file_reader.py
     file_writer.py
 
Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).


# Bu fayl geometry papkasini Python paketi sifatida belgilaydi.
# Bo‘sh qoldirilishi mumkin, chunki faqat paket ekanligini bildiradi.

# Aylana bilan bog‘liq matematik hisob-kitoblarni amalga oshiruvchi modul
from math import pi  # Matematik pi konstantasini import qilamiz

def calculate_area(radius):
    """Aylananing yuzasini hisoblaydi (Formula: π * r²)"""
    # Radiusning kvadratini pi ga ko‘paytirib, yuzani hisoblaymiz
    return pi * radius ** 2

def calculate_circumference(radius):
    """Aylananing aylana uzunligini hisoblaydi (Formula: 2 * π * r)"""
    # Radiusni 2 ga va pi ga ko‘paytirib, aylana uzunligini hisoblaymiz
    return 2 * pi * radius

# Fayldan ma'lumotlarni o‘qish uchun modul
def read_file(file_path):
    """Berilgan fayl yo‘lidagi fayldan ma'lumotni o‘qiydi"""
    try:
        # Faylni o‘qish rejimida ('r') UTF-8 kodlash bilan ochamiz
        with open(file_path, 'r', encoding='utf-8') as file:
            # Faylning butun mazmunini o‘qiymiz
            content = file.read()
        # O‘qilgan mazmunni qaytaramiz
        return content
    except FileNotFoundError:
        # Agar fayl topilmasa, xato xabarini qaytaramiz
        return "Xato: Fayl topilmadi!"
    except Exception as e:
        # Boshqa xatolar yuz bersa, xato xabarini qaytaramiz
        return f"Xato: {str(e)}"
    
    # Faylga ma'lumot yozish uchun modul
def write_file(file_path, content):
    """Berilgan fayl yo‘liga ma'lumot yozadi"""
    try:
        # Faylni yozish rejimida ('w') UTF-8 kodlash bilan ochamiz
        with open(file_path, 'w', encoding='utf-8') as file:
            # Faylga berilgan content ni yozamiz
            file.write(content)
        # Muvaffaqiyatli yozilganligi haqida xabar qaytaramiz
        return "Faylga muvaffaqiyatli yozildi!"
    except Exception as e:
        # Xato yuz bersa, xato xabarini qaytaramiz
        return f"Xato: {str(e)}"
    
    # Geometriya va fayl operatsiyalarini sinash uchun asosiy skript
from geometry.circle import calculate_area, calculate_circumference  # Aylana funksiyalarini import qilamiz
from file_operations.file_writer import write_file  # Faylga yozish funksiyasini import qilamiz
from file_operations.file_reader import read_file  # Fayldan o‘qish funksiyasini import qilamiz

# Geometriya sinovi
r = 5  # Aylana radiusi sifatida 5 ni olamiz
print(f"Radius: {r}")  # Radiusni chop etamiz
print("Yuza:", calculate_area(r))  # Aylana yuzasini hisoblaymiz va chop etamiz
print("Aylana uzunligi:", calculate_circumference(r))  # Aylana uzunligini hisoblaymiz va chop etamiz

# Fayl operatsiyalari sinovi
filename = "test.txt"  # Yozish va o‘qish uchun fayl nomi
# Faylga aylana radiusi va yuzasi haqida ma'lumot yozamiz
write_result = write_file(filename, f"Aylana radiusi: {r}\nYuza: {calculate_area(r)}")
print(write_result)  # Yozish natijasini chop etamiz
content = read_file(filename)  # Fayldan ma'lumotni o‘qiymiz
print("Fayldan o'qildi:")  # O‘qilgan ma'lumotni chop etishdan oldin xabar
print(content)  # O‘qilgan ma'lumotni chop etamiz

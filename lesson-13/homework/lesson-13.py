# Homework:
# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Step 1: Ask for user's birthdate
birth_input = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    # Step 2: Convert input to datetime object
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    today = datetime.today().date()

    # Check if birthdate is in the future
    if birth_date > today:
        print("You haven't been born yet!")
    else:
        # Step 3: Calculate difference
        age = relativedelta(today, birth_date)

        # Step 4: Display result
        print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")

except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")


# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime, timedelta

# Foydalanuvchidan tug'ilgan sanani olish (YYYY-MM-DD formatida)
birth_input = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    today = datetime.today().date()

    # Keyingi tug'ilgan kun yilini aniqlaymiz
    next_birthday = birth_date.replace(year=today.year)

    # Agar bu yilgi tug'ilgan kun o'tib ketgan bo'lsa, keyingi yilga o'tkazamiz
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    # Qolgan kunlar sonini hisoblaymiz
    days_until = (next_birthday - today).days

    print(f"Your next birthday is in {days_until} days.")

except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")

# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

try:
    current_input = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    hours = int(input("Enter meeting duration hours: "))
    minutes = int(input("Enter meeting duration minutes: "))

    current_datetime = datetime.strptime(current_input, "%Y-%m-%d %H:%M")
    meeting_duration = timedelta(hours=hours, minutes=minutes)
    end_datetime = current_datetime + meeting_duration

    print("Meeting will end on:", end_datetime.strftime("%Y-%m-%d %H:%M"))

except ValueError:
    print("Invalid input. Please use 'YYYY-MM-DD HH:MM' and numeric values for duration.")

# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
import pytz

def list_timezones():
    print("Available timezones examples:")
    print(" - UTC")
    print(" - US/Eastern")
    print(" - Europe/London")
    print(" - Asia/Tashkent")
    print(" - Asia/Kolkata")
    print(" - Australia/Sydney")
    print("For full list visit: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")

try:
    # Sana va vaqtni kiritish (format: YYYY-MM-DD HH:MM)
    user_datetime_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    user_datetime = datetime.strptime(user_datetime_str, "%Y-%m-%d %H:%M")

    # Hozirgi timezone-ni so'rash
    list_timezones()
    from_tz_str = input("Enter your current timezone (e.g. 'Asia/Tashkent'): ")
    to_tz_str = input("Enter timezone to convert to (e.g. 'US/Eastern'): ")

    # Timezone obyektlarini yaratish
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)

    # Hozirgi vaqtga timezone qo'shamiz
    localized_dt = from_tz.localize(user_datetime)

    # Yangi timezone ga o'tkazamiz
    converted_dt = localized_dt.astimezone(to_tz)

    print(f"\nOriginal time ({from_tz_str}): {localized_dt.strftime('%Y-%m-%d %H:%M %Z%z')}")
    print(f"Converted time ({to_tz_str}): {converted_dt.strftime('%Y-%m-%d %H:%M %Z%z')}")

except Exception as e:
    print("Error:", e)
    print("Make sure you entered valid date/time and timezone names.")


# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time

future_input = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")

try:
    future_time = datetime.strptime(future_input, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        if future_time <= now:
            print("Countdown finished!")
            break

        diff = future_time - now

        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time remaining: {days}d {hours}h {minutes}m {seconds}s", end='\r')

        time.sleep(1)

except ValueError:
    print("Invalid date/time format. Please use YYYY-MM-DD HH:MM:SS.")


# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

def is_valid_email(email):
    # Oddiy email regex qoidasi:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address!")
else:
    print("Invalid email address.")


# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

def format_phone_number(number):
    digits = ''.join(filter(str.isdigit, number))

    if len(digits) != 10:
        return f"Invalid phone number. Expected 10 digits, got {len(digits)}."

    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


phone_input = input("Enter your phone number: ")
formatted = format_phone_number(phone_input)
print("Formatted phone number:", formatted)



# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

def check_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not any(c.isupper() for c in password):
        return "Password must contain at least one uppercase letter."

    if not any(c.islower() for c in password):
        return "Password must contain at least one lowercase letter."

    if not any(c.isdigit() for c in password):
        return "Password must contain at least one digit."

    return "Password is strong."

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)

# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

def find_word_occurrences(text, word):
    word = word.lower()
    text_lower = text.lower()

    start = 0
    occurrences = []

    while True:
        pos = text_lower.find(word, start)
        if pos == -1:
            break
        occurrences.append(pos)
        start = pos + len(word)

    return occurrences

sample_text = """
Python is an amazing programming language. Python allows you to write clean and readable code.
Many developers love Python for its simplicity.
"""

word_to_find = input("Enter the word to find: ")

positions = find_word_occurrences(sample_text, word_to_find)

if positions:
    print(f"The word '{word_to_find}' was found at positions: {positions}")
else:
    print(f"The word '{word_to_find}' was not found in the text.")

# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re
from datetime import datetime

def is_valid_date(date_str, fmt):
    try:
        datetime.strptime(date_str, fmt)
        return True
    except ValueError:
        return False

def extract_dates(text):
    # 2 ta format uchun regex (DD/MM/YYYY va YYYY-MM-DD)
    pattern1 = r'\b(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-](\d{4})\b'
    pattern2 = r'\b(\d{4})[\/\-](0?[1-9]|1[012])[\/\-](0?[1-9]|[12][0-9]|3[01])\b'

    matches1 = re.findall(pattern1, text)
    matches2 = re.findall(pattern2, text)

    dates = []

    for d in matches1:
        date_str = f"{d[0]}/{d[1]}/{d[2]}"
        if is_valid_date(date_str, "%d/%m/%Y"):
            dates.append(date_str)

    for d in matches2:
        date_str = f"{d[0]}-{d[1]}-{d[2]}"
        if is_valid_date(date_str, "%Y-%m-%d"):
            dates.append(date_str)

    return dates

text_input = input("Enter some text containing dates: ")
results = extract_dates(text_input)

if results:
    print("Found dates:")
    for date in results:
        print(date)
else:
    print("No valid dates found.")














Homework:

Exercise 1: Threaded Prime Number Checker

Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

import threading
import math

lock = threading.Lock()

def is_prime(n):
    """
    Berilgan son tub ekanligini tekshiradi.
    2 dan kichik sonlar tub emas.
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result_list):
    """
    Diapazondagi sonlarni tekshiradi va tub sonlarni umumiy ro‘yxatga qo‘shadi.
    Natijaga kirish paytida lock ishlatiladi.
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    with lock:
        result_list.extend(primes)

def main():
    start_range = 1
    end_range = 100
    num_threads = 4

    threads = []
    results = []

    range_size = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        start = start_range + i * range_size
        end = start_range + (i + 1) * range_size - 1 if i != num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes, args=(start, end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results.sort()
    print(f"{start_range} dan {end_range} gacha bo‘lgan tub sonlar:")
    print(results)

if __name__ == "__main__":
    main()



Exercise 2: Threaded File Processing

Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

import threading
from collections import Counter
import string

counter_lock = threading.Lock()

def clean_word(word):
    """
    So‘zdagi punktuatsiya belgilarini olib tashlaydi va kichik harflarga o‘giradi.
    """
    return word.strip(string.punctuation).lower()

def count_words(lines, counter):
    """
    Berilgan satrlarni hisoblab, so‘zlar sonini global counterga qo‘shadi.
    Lock yordamida raqobat oldini oladi.
    """
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        cleaned_words = [clean_word(word) for word in words if clean_word(word)]
        local_counter.update(cleaned_words)
    with counter_lock:
        counter.update(local_counter)

def main():
    filename = "large_text_file.txt"
    num_threads = 4

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    lines_per_thread = total_lines // num_threads

    threads = []
    total_counter = Counter()

    for i in range(num_threads):
        start = i * lines_per_thread
        end = (i + 1) * lines_per_thread if i != num_threads - 1 else total_lines
        thread_lines = lines[start:end]
        thread = threading.Thread(target=count_words, args=(thread_lines, total_counter))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Fayldagi so‘zlar soni bo‘yicha umumiy natija:")
    for word, count in total_counter.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

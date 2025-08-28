# 1
def modify_string(txt):
    vowels = "aeiou"
    result = []
    i = 0
    count = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            if txt[i] not in vowels and (i + 1 < len(txt) and txt[i+1] != "_"):
                result.append("_")
            count = 0
        i += 1
    return "".join(result)

print("Task 1:")
print(modify_string("hello"))          
print(modify_string("assalom"))        
print(modify_string("abcabcabcdeabcdefabcdefg"))
print("\n")
# 2
print("Task 2:")
n = int(input("Enter an integer n (1-20): "))
for i in range(n):
    print(i**2)
print("\n")

#3
print("Task 3:")

# Exercise 1
print("Exercise 1:")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

# Exercise 2
print("Exercise 2:")
for i in range(1, 6):
    print(*range(1, i+1))
print()

# Exercise 3
n_sum = int(input("Enter number for sum: "))
print("Sum is:", sum(range(1, n_sum+1)))
print()

# Exercise 4
num_table = int(input("Enter number for multiplication table: "))
print("Multiplication table:")
print(*[num_table * i for i in range(1, 11)])
print()

# Exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]
print("Exercise 5:")
for num in numbers:
    if num % 5 == 0 and num < 200:
        print(num)
print()

# Exercise 6
num_digits = int(input("Enter number to count digits: "))
print("Number of digits:", len(str(num_digits)))
print()

# Exercise 7
print("Exercise 7:")
n_rp = 5
for i in range(n_rp, 0, -1):
    print(*range(i, 0, -1))
print()

# Exercise 8
list1 = [10, 20, 30, 40, 50]
print("Exercise 8:")
for x in reversed(list1):
    print(x)
print()

# Exercise 9
print("Exercise 9:")
for i in range(-10, 0):
    print(i)
print()

# Exercise 10
print("Exercise 10:")
for i in range(5):
    print(i)
else:
    print("Done!")
print()

# Exercise 11
print("Exercise 11: Prime numbers 25 to 50")
for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print("\n")

# Exercise 12
print("Exercise 12: Fibonacci sequence")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# Exercise 13
n_fact = int(input("Enter number for factorial: "))
fact = 1
for i in range(1, n_fact+1):
    fact *= i
print(f"{n_fact}! =", fact)
print("\n")

# 4
def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for key in set(list1 + list2):
        diff = abs(c1.get(key, 0) - c2.get(key, 0))
        result.extend([key]*diff)
    return result

print("Task 4:")
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))

# Q01. Find the data type of every value in a mixed list.

values = [10, 20.5, "Python", True, 5+3j, [1, 2], (3, 4), {1, 2}]

for value in values:
    print(value, ":", type(value))

# Q02. Convert a nested list into a tuple of tuples.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = tuple(tuple(row) for row in nested_list)

print("Tuple of tuples:", result)

# Q03. Remove all duplicate values from a mixed list while preserving the original order.

values = [10, "Python", 20, 10, "Java", 20, "Python", 30]

result = []

for value in values:
    if value not in result:
        result.append(value)

print("List after removing duplicates:", result)


# Q04. Check whether a number is a power of 2 using operators.

num = int(input("Enter a number: "))

if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")

# Q05. Swap two numbers using bitwise XOR.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("First number:", a)
print("Second number:", b)


# Q06. Find whether a number is divisible by both 4 and 6 using logical operators.

num = int(input("Enter a number: "))

if num % 4 == 0 and num % 6 == 0:
    print("Number is divisible by both 4 and 6")
else:
    print("Number is not divisible by both 4 and 6")


# Q07. Calculate the total electricity bill using different unit rates.
# Assumed rates:
# First 100 units = Rs. 5 per unit
# Next 100 units = Rs. 7 per unit
# Above 200 units = Rs. 10 per unit

units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    print("Electricity bill: Rs.", bill)
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    print("Electricity bill: Rs.", bill)

# Q08. Check whether three sides can form a triangle.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")


# Q09. Determine the type of triangle (Equilateral, Isosceles, Scalene).

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


# Q10. Create a simple ATM menu (Withdraw, Deposit, Balance).

balance = 5000

while True:
    print("\n----- ATM MENU -----")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful")
        else:
            print("Enter a valid amount")

    elif choice == 3:
        print("Available balance: Rs.", balance)

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")


# Q13. Print all prime numbers between 1 and n.

n = int(input("Enter the value of n: "))

print("Prime numbers:")

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

# Q14. Find the factorial of a number using a loop.

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial:", factorial)


# Q15. Print the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Q16. Check whether a number is an Armstrong number.

num = int(input("Enter a number: "))

if num < 0:
    print("Not an Armstrong number")
else:
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

# Q17. Reverse a number and check if it is a palindrome.

num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers are not considered palindromes")
else:
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reversed number:", reverse)

    if original == reverse:
        print("Palindrome number")
    else:
        print("Not a palindrome number")

# Q18. Find the Greatest Common Divisor (GCD) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

num1 = abs(a)
num2 = abs(b)

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD:", num1)

# Q19. Write a function to check if a string is a palindrome.

def is_palindrome(text):
    text = text.lower()

    return text == text[::-1]


word = input("Enter a string: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")


# Q20. Write a function to count vowels and consonants in a string.

def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


text = input("Enter a string: ")

v, c = count_vowels_consonants(text)

print("Vowels:", v)
print("Consonants:", c)


# Q21. Create a function to calculate simple and compound interest.

def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100

    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal

    return simple_interest, compound_interest


p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

if p < 0 or r < 0 or t < 0:
    print("Invalid input")
else:
    si, ci = calculate_interest(p, r, t)

    print("Simple Interest:", si)
    print("Compound Interest:", ci)


# Q22. Write a function to return all factors of a number.

def factors(n):
    result = []

    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.append(i)

    return result


num = int(input("Enter a number: "))

if num == 0:
    print("Every non-zero integer is a factor of zero")
else:
    print("Factors:", factors(num))


# Q23. Write a function to find the second-largest number in a list.

def second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second


numbers = [10, 25, 40, 15, 30]

result = second_largest(numbers)

if result is None:
    print("Second largest number does not exist")
else:
    print("Second largest number:", result)


# Q24. Merge two lists without duplicates.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for num in list1 + list2:
    if num not in result:
        result.append(num)

print("Merged list:", result)


# Q25. Find the second-largest and second-smallest elements.

numbers = [10, 20, 30, 40, 50]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

if len(unique_numbers) < 2:
    print("Second largest and second smallest do not exist")
else:
    smallest = unique_numbers[0]
    second_smallest = None
    largest = unique_numbers[0]
    second_largest = None

    for num in unique_numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num != smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num

        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num

    print("Second smallest:", second_smallest)
    print("Second largest:", second_largest)


# Q26. Rotate a list to the left by k positions.

numbers = [1, 2, 3, 4, 5]

k = int(input("Enter number of rotations: "))

if len(numbers) > 0:
    k = k % len(numbers)

    rotated_list = numbers[k:] + numbers[:k]

    print("Original list:", numbers)
    print("Rotated list:", rotated_list)
else:
    print("List is empty")


# Q27. Separate even and odd numbers into two lists.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)


# Q28. Find the common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)

# Q29. Count the frequency of each element in a tuple.

numbers = (1, 2, 3, 2, 4, 1, 2, 5, 3)

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element frequencies:")

for key, value in frequency.items():
    print(key, ":", value)

# Q30. Find the union, intersection, and difference of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))


# Q31. Check whether one set is a subset of another.

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")


# Q32. Count the frequency of words in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:")

for word, count in frequency.items():
    print(word, ":", count)


# Q33. Create a dictionary from two lists (keys and values).

keys = ["Name", "Age", "City"]
values = ["Ketaki", 21, "Nashik"]

result = dict(zip(keys, values))

print("Dictionary:", result)

# Q34. Sort a dictionary by its values.

data = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 80,
    "Orange": 40
}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:")

for key, value in sorted_data.items():
    print(key, ":", value)


# Q35. Read a text file and count the number of lines, words, and characters.

filename = "sample.txt"

try:
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", characters)

except FileNotFoundError:
    print("File not found")


# Q36. Copy only the even-numbered lines from one file to another.

source_file = "input.txt"
destination_file = "output.txt"

try:
    with open(source_file, "r") as source:
        lines = source.readlines()

    with open(destination_file, "w") as destination:
        for i, line in enumerate(lines, start=1):
            if i % 2 == 0:
                destination.write(line)

    print("Even-numbered lines copied successfully")

except FileNotFoundError:
    print("Source file not found")

# Q37. Handle invalid integer input using try-except.

try:
    num = int(input("Enter an integer: "))
    print("Entered number:", num)

except ValueError:
    print("Invalid input! Please enter an integer.")

# Q38. Handle file-not-found errors while reading a file.

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")


# Q39. Create a random password generator using the random and string modules.

import random
import string

length = int(input("Enter password length: "))

if length <= 0:
    print("Enter a valid password length")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    print("Generated password:", password)


# Q40. Use the datetime module to calculate the number of days between two dates.

from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

try:
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")

    difference = abs((d2 - d1).days)

    print("Number of days between dates:", difference)

except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY.")



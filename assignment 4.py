# Q01. Write a Python program to check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Q02. Write a program to find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


# Q03. Write a program to check whether a given number is prime.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


# Q04. Write a program to print the Fibonacci series up to n terms.

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


# Q05. Write a program to find the factorial of a number using a loop.

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial:", factorial)


# Q06. Write a program to reverse a string without using [::-1].

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)


# Q07. Write a program to check whether a string is a palindrome.

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text.lower() == reverse.lower():
    print("Palindrome")
else:
    print("Not a palindrome")


# Q08. Write a program to count the number of vowels and consonants in a string.

text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# Q09. Write a program to find the sum of all elements in a list.

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("Sum of list elements:", total)


# Q10. Write a program to find the largest and smallest element in a list
# without using max() or min().

numbers = [25, 10, 45, 5, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest element:", largest)
print("Smallest element:", smallest)


# Q11. Write a program to remove duplicate elements from a list.

numbers = [10, 20, 30, 20, 40, 10, 50]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)


# Q12. Write a program to count how many times each element appears
# in a list using a dictionary.

numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element Frequency:")

for key, value in frequency.items():
    print(key, ":", value)


# Q13. Write a program to find the second-largest number in a list.

numbers = [10, 25, 40, 15, 30]

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num

    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

if second_largest is None:
    print("Second-largest number does not exist")
else:
    print("Second-largest number:", second_largest)


# Q16. Write a program to find the frequency of each character in a string.

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")

for key, value in frequency.items():
    print(key, ":", value)


# Q18. Write a program to find all duplicate values in a list.

numbers = [10, 20, 30, 10, 40, 20, 50, 30]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate values:", duplicates)


# Q19. Write a program that takes a sentence and finds the longest word.

sentence = input("Enter a sentence: ")

words = sentence.split()

if len(words) == 0:
    print("No words found")
else:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)
    print("Length:", len(longest))


# Q20. Create a simple student marks program that:
# a. Accepts marks for 5 subjects.
# b. Calculates the total and percentage.
# c. Assigns a grade.
# d. Displays whether the student passed or failed.
#
# Assumptions:
# Minimum passing marks = 35 in each subject.
# Grade A = 90 and above
# Grade B = 80 to 89
# Grade C = 70 to 79
# Grade D = 60 to 69
# Grade F = Below 60

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter marks between 0 and 100.")
        break

    marks.append(mark)

if len(marks) == 5:
    total = sum(marks)
    percentage = total / 5

    print("\n----- STUDENT RESULT -----")
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

    if any(mark < 35 for mark in marks):
        grade = "F"
        print("Grade:", grade)
        print("Result: FAIL")

    else:
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)
        print("Result: PASS")
# Q01. Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(is_even(num))

# Q02. Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.

def largest(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Largest number:", largest(num1, num2))


# Q03. Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

num = int(input("Enter a number: "))
print_numbers(num)


# Q04. Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

num = int(input("Enter a number: "))
print("Sum:", sum_n(num))


# Q05. Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
table(num)


# Q06. Count Even Numbers
# Write a function that takes a list and returns how many even numbers it contains.
# Example: count_even([1, 2, 3, 4, 6])
# Output: 3

def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count

numbers = [1, 2, 3, 4, 6]
print("Even numbers count:", count_even(numbers))


# Q07. Find Maximum
# Without using max(), write a function that returns the largest number in a list.

def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = [10, 25, 5, 40, 15]
print("Largest number:", find_max(numbers))


# Q11. FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()


# Q12. Palindrome Checker
# Write a function that returns True if a string is a palindrome.

def is_palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False

word = input("Enter a string: ")
print("Palindrome:", is_palindrome(word))


# Q13. Count Vowels
# Write a function that counts the vowels in a string.

def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))


# Q14. Second Largest Number
# Write a function that returns the second largest number in a list without using sort().

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
print("Second largest number:", second_largest(numbers))

# Q15. Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

import random

def guessing_game():
    secret_number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret_number:
            print("Congratulations! You guessed it correctly.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guessing_game()


# Q16. Grade Function
# Write a function grade(marks) that:
# Returns "A" for marks >= 90
# Returns "B" for marks >= 80
# Returns "C" for marks >= 70
# Returns "D" for marks >= 60
# Otherwise returns "F"

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks = int(input("Enter your marks: "))
print("Your grade is:", grade(marks))




#Q1. Check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")


#Q2. Check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

#Q3. Find the greater of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
else:
    print("Both numbers are equal")

#Q4. Find the greatest of three numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("First number is greatest")
elif num2 >= num1 and num2 >= num3:
    print("Second number is greatest")
else:
    print("Third number is greatest")

#Q5. Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Q6. Check whether a year is a leap year.
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#Q7. Check if a character is a vowel or consonant.
ch = input("Enter an alphabet: ")

if ch.lower() in "aeiou" and len(ch) == 1:
    print("Vowel")
elif ch.isalpha() and len(ch) == 1:
    print("Consonant")
else:
    print("Please enter a single alphabet")

#Q7. Check if a character is a vowel or consonant.
ch = input("Enter an alphabet: ")

if ch.lower() in "aeiou" and len(ch) == 1:
    print("Vowel")
elif ch.isalpha() and len(ch) == 1:
    print("Consonant")
else:
    print("Please enter a single alphabet")

#Q8. Check whether a number is divisible by 5 and 11.
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")

#Q9. Check if a number is a multiple of both 3 and 7.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Number is a multiple of both 3 and 7")
else:
    print("Number is not a multiple of both 3 and 7")


#Q10. Assign grades based on marks:
#90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F
marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 0:
    print("Grade F")
else:
    print("Invalid marks")

#Q11. Check if a character is uppercase or lowercase.
ch = input("Enter a character: ")

if len(ch) == 1 and ch.isupper():
    print("Uppercase character")
elif len(ch) == 1 and ch.islower():
    print("Lowercase character")
else:
    print("Please enter a single alphabet")

#Q12. Find whether the entered alphabet is a vowel using if-elif.
ch = input("Enter an alphabet: ").lower()

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Consonant")

#Q13. Check if three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")

#Q14. Determine the type of triangle (Equilateral, Isosceles, Scalene).

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")
elif a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#Q15. Find the largest among four number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("First number is largest")
elif b >= a and b >= c and b >= d:
    print("Second number is largest")
elif c >= a and c >= b and c >= d:
    print("Third number is largest")
else:
    print("Fourth number is largest")

#Q16. Check whether a number is a three-digit number.
num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print("Three-digit number")
elif num <= -100 and num >= -999:
    print("Three-digit number")
else:
    print("Not a three-digit number")

#Q17. Calculate electricity bill using slab rates.
units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity Bill:", bill)
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    print("Electricity Bill:", bill)
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    print("Electricity Bill:", bill)

#Q18. Calculate income tax based on income slabs.
income = float(input("Enter your annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

if income >= 0:
    print("Income Tax:", tax)

#Q19. Check if a student passes (minimum 35 marks in each subject).
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    print("Student is Pass")
else:
    print("Student is Fail")


#Q20. Find whether a number is within a given range.
num = int(input("Enter a number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

if lower <= num <= upper:
    print("Number is within the range")
else:
    print("Number is outside the range")


#Q21. Build a simple calculator using if-elif-else (+, -, *, /).
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print("Addition:", num1 + num2)
elif operator == '-':
    print("Subtraction:", num1 - num2)
elif operator == '*':
    print("Multiplication:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

#Q22. Check if a year is a century leap year.
year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century Leap Year")
elif year % 100 == 0:
    print("Century year but not a Leap Year")
else:
    print("Not a Century Year")


#Q23. Determine the season based on the month number.
month = int(input("Enter month number (1-12): "))

if month == 3 or month == 4 or month == 5:
    print("Summer Season")
elif month == 6 or month == 7 or month == 8 or month == 9:
    print("Monsoon Season")
elif month == 10 or month == 11:
    print("Autumn Season")
elif month == 12 or month == 1 or month == 2:
    print("Winter Season")
else:
    print("Invalid month number")


#Q24. Find the number of days in a month.
month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
else:
    print("Invalid month")

#Q25. Check whether a password meets minimum conditions (length, digits, etc.).
password = input("Enter your password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Password is valid")
else:
    print("Password is invalid")
    print("Password must contain at least 8 characters and one digit")

#Q26. Determine ticket price based on age category.
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket is Free")
elif age <= 17:
    print("Ticket Price: Rs. 100")
elif age <= 59:
    print("Ticket Price: Rs. 200")
else:
    print("Ticket Price: Rs. 150")

#Q27. Calculate discount based on purchase amount.
amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount < 1000:
    discount = 0
elif amount < 5000:
    discount = amount * 0.05
elif amount < 10000:
    discount = amount * 0.10
else:
    discount = amount * 0.15

if amount >= 0:
    print("Discount:", discount)
    print("Final Amount:", amount - discount)
#Q28. Check if a person is eligible for a driving license (age and eyesight condition).
age = int(input("Enter your age: "))
eyesight = input("Is your eyesight condition satisfactory? (yes/no): ").lower()

if age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

#Q29. Create a login system with username and password validation.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#Q30. Create a menu-driven program using if-elif-else with options like:
print("----- MENU -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Addition:", a + b)

elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Subtraction:", a - b)

elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Multiplication:", a * b)

elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

elif choice == 5:
    print("Exiting program")

else:
    print("Invalid choice")
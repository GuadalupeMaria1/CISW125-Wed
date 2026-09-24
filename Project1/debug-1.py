#Thomas Pangelinan

# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.

total = 0
#First change all output numbers to integers.
num1 = int(input("What's the first number? >"))
total += num1
#After that change all the total numbers to += that way it adds it to the total number
num2 = int(input("What's the second number? >"))
total += num2
num3 = int(input("What's the third number? >"))
total += num3
print(f"Total is: {total}")
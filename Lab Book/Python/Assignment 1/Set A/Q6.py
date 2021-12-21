"""
Write a program to calculate sum of first and last digit of a number.
"""

number = input("Enter the number: ")

total = int(number[0]) + int(number[-1])
print(total)
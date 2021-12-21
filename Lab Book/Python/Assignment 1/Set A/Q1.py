"""
Write python script to calculate sum of digits of a given input number
"""

def calculate_sum_of_digits(num):
    sum = 0

    for digit in str(num):
      sum += int(digit)
    return sum


number = input("Enter a number: ")
sum_of_digits = calculate_sum_of_digits(number)
print(sum_of_digits)
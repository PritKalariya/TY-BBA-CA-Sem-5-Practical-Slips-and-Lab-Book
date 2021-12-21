"""
Write python script to check whether a input number is perfect number of not.
"""

def isPerfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        return "Perfect Number."
    else:
        return "Not a perfect NUmber."


number = int(input("Enter  anumber: "))
print(isPerfect(number))
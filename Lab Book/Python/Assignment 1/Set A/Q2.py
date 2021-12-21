"""
Write python script to check whether a input number is Armstrong number or not.
"""

def check_armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum += rem ** 3
        temp //= 10

    if sum == num:
        return "Armstrong Number."
    else:
        return "Not an Armstrong Number."


number =  int(input("Enter a number: "))
print(check_armstrong(number))
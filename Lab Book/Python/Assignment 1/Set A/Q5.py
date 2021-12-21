"""
Write a program to check whether a input number is palindrome or not.
"""

def check_palindrome(num):
    temp = num
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev*10 + rem
        temp //= 10

    if rev == num:
        return "palindrome Number."
    else:
        return "Not an palindrome Number."


number =  int(input("Enter a number: "))
print(check_palindrome(number))
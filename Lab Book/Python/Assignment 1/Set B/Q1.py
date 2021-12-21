"""
Write a program to accept a number and count number of even, odd, zero digits within that number.
"""

def counter(n):
    odd = 0
    even = 0
    zero = 0

    for i in n:
        if int(i) == 0:
            zero += 1
        elif int(i) % 2  != 0:
            odd += 1
        elif int(i) % 2  == 0:
            even += 1

    print(f"Even: {even}\nOdd: {odd}\nZero: {zero}")


number = input("Enter a number: ")
counter(number)
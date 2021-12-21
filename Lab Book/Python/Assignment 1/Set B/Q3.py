"""
Write a program which accepts an integer value as command line and print “Ok” if value is between 1 to 50 (both inclusive) otherwise it prints ”Out of range”.
"""

number = int(input("Enter a number: "))
if number > 0 and number < 51:
    print("Ok")
else:
    print("Out of range")
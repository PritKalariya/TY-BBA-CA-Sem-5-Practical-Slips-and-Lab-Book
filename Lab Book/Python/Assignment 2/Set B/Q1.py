"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
    Sample String : 'General12'
    Expected Result : 'Ge12'

    Sample String : 'Ka'
    Expected Result : 'KaKa'

    Sample String : 'K'
    Expected Result : Empty String
"""

str = input("Enter a string: ")

if len(str) >= 2:
    expected_str = str[0:3] + str[-3:]
else:
    expected_str = "Empty String"

print(expected_str)
"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
    Sample String : 'abc', 'xyz'
    Expected Result : 'xycabz'
"""

str_1 = input("Enter string 1: ")
str_2 = input("Enter string 2: ")

new_str = str_2[0:2] + str_1[2:] + str_1[0:2] + str_2[2:]

print(new_str)
"""
Write a Python program to remove the characters which have odd index values of a given string.
"""

org_str = input("Enter a string: ")

result = ""
for i in range(len(org_str)):
    if i % 2 != 0:
        result = result + org_str[i]

print(result)
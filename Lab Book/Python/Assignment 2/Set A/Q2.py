"""
Write a python script to count the number of characters (character frequency) in a string. Sample String : google.com'. Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}.
"""

org_str = input("Enter a string: ")

char_count = {}
for char in org_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(str(char_count))
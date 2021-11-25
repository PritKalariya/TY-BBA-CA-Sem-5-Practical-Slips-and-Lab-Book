"""
Write a python program to count repeated characters in a string.
    Sample string: 'thequickbrownfoxjumpsoverthelazydog'
    Expected output:
        o 4
        e 3
        u 2
        h 2
        r 2
        t 2
"""

str = input("Enter a string: ")

char_count = {}
for char in str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
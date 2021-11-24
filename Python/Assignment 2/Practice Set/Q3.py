"""
Write a python program to count vowels and consonants in a string.
"""

org_str = input("Enter a string: ")

vowels = 0
consonents = 0
for alphabet in org_str:
    if alphabet in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1
    else:
        consonents += 1

print(f"vowels = {vowels} \nconsonents = {consonents}")
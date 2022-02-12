# Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.

dict = {'a': 1, 'b': 2, 'c': 3}

user_key = input("Enter key: ")

if user_key in dict.keys():
    dict[user_key] = 'new value'

print(dict)
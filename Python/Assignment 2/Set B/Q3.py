"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

str = input("Enter a sentence: ")

print(word_count(str))
# Write a Python script using class to reverse a string word by word

class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        self.words = self.string.split()
        self.reversed_words = self.words[::-1]
        self.reversed_string = ' '.join(self.reversed_words)
        return self.reversed_string


string = input('Enter a string: ')
string_obj = String(string)
print(string_obj.reverse())
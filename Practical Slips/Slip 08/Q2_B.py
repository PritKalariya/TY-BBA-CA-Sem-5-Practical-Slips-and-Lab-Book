# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case. Further modify the program to reverse a string word by word and print it in lower case.


class String:

    def get_string(self):
        self.string = input("Enter the string: ")

    def print_string(self):
        return self.string.upper()

    def reverse_string(self):
        return self.string[::-1]


string_obj = String()
string_obj.get_string()
print(f"The string in upper case is: {string_obj.print_string()}")
print(f"The string in reverse is: {string_obj.reverse_string()}")
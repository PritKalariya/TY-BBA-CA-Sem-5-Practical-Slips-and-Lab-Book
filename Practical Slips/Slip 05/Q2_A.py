#  Write a Python script using class, which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.


class Q2_A:
    def get_string(self):
        self.string = (input("Enter a string: ")).upper()

    def print_string(self):
        print(self.string)


new_str = Q2_A()
new_str.get_string()
new_str.print_string()
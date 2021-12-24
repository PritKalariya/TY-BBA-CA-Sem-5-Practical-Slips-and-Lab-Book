class Q2_A:
    def get_string(self):
        self.string = (input("Enter a string: ")).upper()

    def print_string(self):
        print(self.string)


new_str = Q2_A()
new_str.get_string()
new_str.print_string()
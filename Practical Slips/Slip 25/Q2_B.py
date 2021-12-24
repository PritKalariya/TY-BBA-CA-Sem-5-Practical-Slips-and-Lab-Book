class Calculator:
    def add(self, a, b):
        return a + b

    def susbtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a*b

    def division(self, a, b):
        return a/b


my_cal = Calculator()

addition = my_cal.add(10, 20)
substraction = my_cal.susbtract(50, 20)
mult = my_cal.multiply(2, 3)
div = my_cal.division(50, 2)

print(f"Addition = {addition}\nSubstrcation = {substraction}\nMultiplication = {mult}\nDivision = {div}")
# Write a python script to define a class student having members roll no, name, age, gender. Create a subclass called Test with member marks of 3 subjects. Create three objects of the Test class and display all the details of the student with total marks.


class Student:
    def __init__(self, roll_no, name, age, gender, m1, m2, m3):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.m1 = int(m1)
        self.m2 = int(m2)
        self.m3 = int(m3)

class Test(Student):
    def total_marks(self):
        return self.m1 + self.m2 + self.m3

    def display_details(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Total marks: ", self.total_marks())
        print()


s1 = Test('01', 'a', '20', 'male', '10', '9', '10')
s2 = Test('02', 'b', '19', 'male', '8', '7', '8')
s3 = Test('03', 'c', '20', 'female', '7', '9', '9')

s1.display_details()
s2.display_details()
s3.display_details()
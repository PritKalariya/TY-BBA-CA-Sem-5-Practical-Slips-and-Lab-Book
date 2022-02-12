# Define a class Employee having members id, name, department, salary. Create a subclass called manager with member bonus. Define methods accept and display in both the classes. Create n objects of the manager class and display the details of the manager having the maximum total salary (salary+bonus).


class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def accept(self):
        self.id = int(input("Enter id: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
        self.salary = int(input("Enter salary: "))

    def display(self):
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Department: ", self.department)
        print("Salary: ", self.salary)


class Manager(Employee):
    def __init__(self, id, name, department, salary, bonus):
        Employee.__init__(self, id, name, department, salary)
        self.bonus = bonus

    def accept(self):
        Employee.accept(self)
        self.bonus = int(input("Enter bonus: "))

    def display(self):
        Employee.display(self)
        print("Bonus: ", self.bonus)
        print("Total Salary: ", self.total_salary)
        print("\n")

    def total_salary(self):
        self.total_salary = self.salary + self.bonus
        return self.total_salary

manager = []
manager_total_salary = []

for i in range(int(input("Enter number of employees: "))):
    manager.append(Manager(0, "", "", 0, 0))
    print("\n")
    manager[i].accept()
    manager_total_salary.append(manager[i].total_salary())

print("Employee details: ")
for i in range(len(manager)):
    manager[i].display()

print(f"Higest salary: {max(manager_total_salary)}")
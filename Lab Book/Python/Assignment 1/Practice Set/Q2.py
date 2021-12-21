"""
Write a python script to accepts annual basic salary of an employee and calculates and displays the Income tax as per the following rules.

Basic:   < 2,50,000                 Tax = 0
Basic:  2,50,000 to 5,00,000        Tax = 10%
Basic:  > 5,00,000                  Tax = 20
"""

def calculate_tax(salary):
    salary = int(salary.replace(",", ""))
    if salary < 250000:
        tax = 0
    elif salary >= 250000 and salary <= 500000:
        tax = salary // 10
    else:
        tax = salary // 20
    return tax


basic_salary = input("Enter your basic salary: ")

tax_amount = calculate_tax(basic_salary)

print(f"The total tax payable on {basic_salary} is {tax_amount}.")
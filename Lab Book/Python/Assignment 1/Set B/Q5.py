"""
Write python script to accept two numbers as range and display multiplication table of all numbers within that range.
"""

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{i} X {n} = {i*n}")
    print("\n\n")


number = int(input("Enter a number: "))

for i in range(1, number + 1):
    multiplication_table(i)
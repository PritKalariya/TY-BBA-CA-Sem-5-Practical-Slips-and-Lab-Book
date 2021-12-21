"""
A cashier has currency notes of denomination 1, 5 and 10. Write python script to accept the amount to be withdrawn from the user and print the total number of currency notes of each denomination the cashier will have to give
"""

def notes_counter(amount):
    notes_10 = total_amt // 10
    amount %= 10          # Get the reminder for further calculations

    notes_5 = amount // 5
    amount %= 5

    notes_1 = amount      # The remaining amount will be given in ones
    return notes_10, notes_5, notes_1


total_amt = int(input("Enter the amount to be withdrawn: "))

notes_10, notes_5, notes_1 = notes_counter(total_amt)

print(f"Notes of 10s: {notes_10}")
print(f"Notes of 5s: {notes_5}")
print(f"Notes of 1s: {notes_1}")
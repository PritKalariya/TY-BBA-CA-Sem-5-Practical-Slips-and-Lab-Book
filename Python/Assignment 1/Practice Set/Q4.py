"""
Write a python script to accept the cost price and selling price from the keyboard. Find out if the seller has made a profit or loss and display how much profit or loss has been made.
"""

def calculate_pl(cp, sp):
    if cp > sp:
        loss = cp - sp
        return f"Loss of ${loss}."
    elif cp < sp:
        profit = sp - cp
        return f"Profit of ${profit}."
    else:
        return "No profit No loss."



cost_price = int(input("Enter the Cost Price of the product: "))
selling_price = int(input("Enter the Selling Price of the product: "))

profit_loss = calculate_pl(cost_price, selling_price)
print(profit_loss)
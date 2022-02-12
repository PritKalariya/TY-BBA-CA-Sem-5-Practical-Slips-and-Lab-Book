# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String: 'The quick Brown Fox'
# Expected Output:
    # No. of Upper case characters: 3
    # No. of Lower case characters: 13


def check_upper_lower():
    string = input("Enter a string: ")
    upper_counter = 0
    lower_counter = 0

    for alpha in string:
        if alpha.isupper():
            upper_counter += 1
        if alpha.islower():
            lower_counter += 1

    print(f"Number of Uppercase characters is: {upper_counter}")
    print(f"Number of Lowercase characters is: {lower_counter}")


check_upper_lower()
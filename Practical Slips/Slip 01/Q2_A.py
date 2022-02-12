# Write a Python program to accept n numbers in list and remove duplicates from a list.


def remove_duplicates(ls):
    return list(set(ls))

ls = []

n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    ls.append(int(input(f"Enter the element for poistion {i}: ")))

new_ls = remove_duplicates(ls)
print(f"The list after removing duplicates: {new_ls}")
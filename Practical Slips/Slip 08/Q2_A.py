# Write a python script to find the repeated items of a tuple

def find_duplicates(ls):
    dup_items = []
    for i in range(len(ls)):
        if ls.count(ls[i]) > 1:
            dup_items.append(ls[i])
    return list(set(dup_items))


ls = []
n = int(input("Enter the number of elements in the tuple: "))
for i in range(n):
    ls.append(input(f"Enter the element for position {i}: "))


print(f"The repeated element is {find_duplicates(ls)}")
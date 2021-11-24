"""
Write  a  python  script  which  accepts  5  integer  values  and  prints  “DUPLICATES”  if  any  of the values entered are duplicates otherwise it prints “ALL UNIQUE”. Example: Let 5 integers are (32, 45, 90, 45, 6) then output “DUPLICATES” to be printed.
"""

from typing import Counter

def counter(list):
    dup = Counter(list)
    for num in integers:
        if dup[num] > 1:
            return True
        else:
            return False


integers = []
for i in range(6):
    integers.append(int(input(f"Enter interger {i}: ")))

flag = counter(integers)
if flag:
    print("Duplicate")
else:
    print("Unique")
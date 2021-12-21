"""
Write a python script to generate the following pattern upto n lines
                        1
                    1   2   1
                1   2   3   2   1
            1   2   3   4   3   2   1
"""

def pattern_generator(row):
    for i in range(1, row+1):
        for j in range(1, row + 1 - i):
            print(' ', end='')

        # for increasing pattern
        for j in range(1, i + 1):
            print(j, end='')

        # for decreasing pattern
        for j in range(i - 1, 0, -1):
            print(j, end='')

        # Moving to next line
        print()


row = int(input("Enter number of rows: "))
pattern_generator(row)
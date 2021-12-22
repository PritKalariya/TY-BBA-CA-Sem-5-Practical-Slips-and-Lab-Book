def fin(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


ln = int(input('Enter a number: '))
print(list(fin(ln)))
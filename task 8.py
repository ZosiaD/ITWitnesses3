def econ(n):
    if n < 6:
        e = 300 + 100 * n
    else:
        m = n//6
        e = 300 + 500 * m + n * 100
    return e
n = int(input('Enter number of months: '))
print(econ(n))

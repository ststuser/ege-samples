def F(n):
    if n == 49:
        return 1
    if n > 49:
        return 0
    return F(n + 1) + F(int('1' + bin(n)[2:], base=2))
print(F(4))
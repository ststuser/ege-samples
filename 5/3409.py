
def first(num):
    return (num << 1) % 256


n = 91
n = first(n)
n = first(n)
n = n - 1
n = first(n)
n = first(n)
n = n - 1

print(n)

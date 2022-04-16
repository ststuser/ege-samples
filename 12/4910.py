a = str('КИЛОБИТ')
i = 0
b = ''
while i < len(a):
    c = a[len(a) - 1 - i] # len(a) - 1
    b = b + c
    i = i + 1
print(b)

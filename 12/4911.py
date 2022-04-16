a = str('ВИАНДОТ')
i = len(a) - 1
b = 'М'
while i > 0:
    c = a[i - 1]
    b += c
    i = i - 2
b = str(b) + 'TOP'
print(b)
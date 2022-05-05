
res = []
for i in range(1, 2000):
    for n in range(1, 2000):
        x = i
        y = n
        a = 0
        b = 0
        while x * y > 0:
            if x > 0:
                a = a + 1
            if y > 0 and y % 7 > b:
                b = y % 7
            x = x // 10
            y = y // 7
        if a == 4 and b == 5:
            res.append(i*n)

print(min(res))
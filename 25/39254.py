from math import sqrt

count = 0
for n in range(500000001, 550000000):
    dels = []
    for d in range(2, int(sqrt(n))+1):
        if n % d == 0:
            dels.append(d)
            if n // d != d:
                dels.append(n // d)

    if len(dels) < 5:
        continue
    dels.sort()
    m = 1
    for d in dels[:5]:
        m *= d
    if 0 < m < n:
        print(m)
        count += 1
        if count > 5:
            break
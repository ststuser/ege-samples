
for n in range(10000000):
    if n % 100000 == 0:
        print(n)
    n_s = str(n)
    s1 = 0
    s2 = 0
    for i in range(len(n_s)-1, -1, -1):
        if int(n_s[i]) % 2 == 0:
            s1 += int(n_s[i])
        if i % 2 == 0:
            s2 += int(n_s[i])
    if abs(s1 - s2) == 26:
        print("RESULT: ", n)
        break
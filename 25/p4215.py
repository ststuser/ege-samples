k=0
for i in range (500000, 500050):
    max_d = 0
    condition = False
    for d in range(2, int(i**0.5)+1):
        if i % d == 0:
            if d % 10 == 8 and d != 8:
                max_d = d
                condition = True
                break
            pair = i // d
            if (pair % 10) == 8:
                max_d = i // d
                condition = True
    if condition:
        print (i, max_d)
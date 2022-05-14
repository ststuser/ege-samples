for i in range(35_000_000, 40_000_000):
    a = i
    count = 0
    while a % 2 == 0:
        a //= 2

    if a % a**0.5 == 0:
        for j in range(2, int(a**0.5) - 1):
            if a % j == 0:
                count += 1
                if count > 2:
                    break
    if count == 1:
        print(i)

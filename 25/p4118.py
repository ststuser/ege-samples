cnt = 0
for n in range(450_000, 500_000):
    dels = []
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            dels.append(d)
            zerk = n // d
            if zerk != d:
                dels.append(zerk)

    for d in dels[:]:
        is_primary = True
        for i in range(2, int(d ** 0.5) + 1):
            if d % i == 0:
                is_primary = False
                break
        if not is_primary:
            dels.remove(d)
    if len(dels) < 2:
        continue

    max_d = max(dels)
    min_d = min(dels)

    if (max_d - min_d) % 29 == 11:
        print(n, max_d - min_d)
        cnt += 1
        if cnt == 4:
            break
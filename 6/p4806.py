
cnt = 0

for xs in range(1, 354261000 - 987 + 1):
    x = xs
    n = (354261000 - 987 - xs) // 3 + 1
    n_l = (xs + 987) + 3 * (n - 1)
    n_n = 987 + 8*n
    if n_n//1000 == 231:
        print(n_n)
        cnt += 1

print(cnt)
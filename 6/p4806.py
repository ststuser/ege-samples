import math

cnt = 0

for x in range(1, 354261000 - 987 + 1):
    k = math.ceil((354261000 - 987 - x) / 3) + 1
    n = 987 + 8*(k-1)
    if n//1000 == 231:
        cnt += 1

print(cnt)
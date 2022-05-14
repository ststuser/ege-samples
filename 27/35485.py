f = open('35485-A.txt')
n = int(f.readline())
d = [int(x) for x in f]
max_s = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            if (d[i] + d[j] + d[k]) % 3 == 0:
                max_s = max(max_s, d[i] + d[j] + d[k])
print(max_s)
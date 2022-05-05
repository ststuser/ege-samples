
# for N in range(150000000, 300000000):
#     x = N
#     m = 0
#     n = 0
#     while x % 2 == 0:
#         x //= 2
#         m += 1
#     while x % 3 == 0:
#         x //= 3
#         n += 1
#     if x == 1 and m % 2 == 0 and n % 2 == 1 and n != 0 and m != 0:
#         print(N, m+n)


for m in range(1, 30):
    for n in range(1, 19):
        N = 2**m*3**n
        if 150000000 <= N <= 300000000 and m % 2 == 0 and n % 2 == 1:
            print(N, m+n)

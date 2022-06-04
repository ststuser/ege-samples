for m in range(2, 30, 2):
    for n in range(1, 19, 2):
        N = 2**m*3**n
        if 150000000 <= N <= 300000000:
            print(N, m+n)

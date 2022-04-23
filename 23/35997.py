

def f(n, iter = 0):
    iter += 1
    if iter > 10:
        yield n
        return
    yield from f(n*2, iter)
    yield from f(n*2+1, iter)

print(len(set(f(1))))
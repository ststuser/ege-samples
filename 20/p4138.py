
MAX_ITER = 5


def steps(h):
    return h // 2 if h % 2 == 0 else h - 2, \
            h // 3 if h % 3 == 0 else h - 3


def f(h, iter=0):
    if iter >= MAX_ITER:
        return
    iter += 1
    if h == 1:
        return "W"
    results = [f(x, iter) for x in steps(h)]
    if any([x == "W" for x in results]):
        return "P1"
    if all([x == "P1" for x in results]):
        return "B1"
    if any([x == "B1" for x in results]):
        return "P2"
    if all([x == "P1" or x == "P2" for x in results]):
        return "B1/2"

for s in range(1, 38):
    if f(s) == "P2":
        print(s)

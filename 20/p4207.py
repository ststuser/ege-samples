
MAX_ITER = 5


def steps(h):
    return h + 3, h + 13, h + 23


def f(h, iter=0):
    if iter >= MAX_ITER:
        return
    iter += 1
    if h >= 73:
        return "W"
    next_steps = [f(x, iter) for x in steps(h)]
    if any([x == "W" for x in next_steps]):
        return "P1"
    if all([x == "P1" for x in next_steps]):
        return "B1"
    if any([x == "B1" for x in next_steps]):
        return "P2"
    if all([x == "P2" for x in next_steps]):
        return "B2"
    if all([x == "P1" or x == "P2" for x in next_steps]):
        return "B1/2"
    return


for s in range(1, 24):
    h = sum([2, s, s*2])
    if f(h) == "B1/2":
        print(s)

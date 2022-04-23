MAX_TURNS = 5


def moves(h: tuple):
    x, sup = h
    if sup:
        return (x + 2, sup), (x * 2, sup)
    else:
        return (x + 2, False), (x * 2, False), (x, True)


def f(h: tuple, turn = 0):
    if turn > MAX_TURNS:
        return
    turn += 1
    results = [f(x, turn) for x in moves(h)]
    if h[0] >= 20:
        return "W"
    if any(x == "W" for x in results):
        return "P1" # Обозначает что текущий игрок выигрывает своим первым ходом
    if all(x == "P1" for x in results):
        return "B1" # Текущий игрок проиграет следующему
    if any(x == "B1" for x in results):
        return "P2"
    if all(x == "P1" or x == "P2" for x in results):
        return "B1/2" # Текущий игрок проиграет следующему 1 или 2 ходом


for s in range(1, 19):
    h = (s, False)
    if f(h) == "B1/2":
        print(s)

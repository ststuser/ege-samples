MAX_TURNS = 10


def moves(h: tuple):
    x, prev_turn = h #h[0], h[1]

    if prev_turn == 1:
        return (x + 2, 2), (x * 3, 3)
    elif prev_turn == 2:
        return (x + 1, 1), (x * 3, 3)
    elif prev_turn == 3:
        return (x + 1, 1), (x + 2, 2)
    else:
        return (x + 1, 1), (x + 2, 2), (x * 3, 3)


def f(h: tuple, turn = 0):
    if turn > MAX_TURNS:
        return
    turn += 1
    results = [f(x, turn) for x in moves(h)]
    if h[0] >= 140:
        return "W"
    if any(x == "W" for x in results):
        return "P1" # Обозначает что текущий игрок выигрывает своим первым ходом
    if all(x == "P1" for x in results):
        return "B1" # Текущий игрок проиграет следующему
    if any(x == "B1" for x in results):
        return "P2"
    if all(x == "P1" or x == "P2" for x in results):
        return "B1/2" # Текущий игрок проиграет следующему 1 или 2 ходом


for s in range(1, 139):
    h = (s, False)
    if f(h) == "B1/2":
        print(s)

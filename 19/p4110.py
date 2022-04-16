MAX_TURNS = 5


def moves(h: int):
    return h + 1, h * 3


def f(h, turn = 0):
    if turn > MAX_TURNS:
        return
    turn += 1
    if 56 <= h <= 80:
        return "W"
    if h > 81:
        return "L"
    results = [f(x, turn) for x in moves(h)]

    if any(x == "W" for x in results):
        return "P1" # Обозначает что текущий игрок выигрывает своим первым ходом
    if all(x == "P1" or x == "L" for x in results):
        return "B1" # Текущий игрок проиграет следующему
    if any(x == "B1" for x in results):
        return "P2"
    if all(x == "P1" or x == "P2" or x == "L" for x in results):
        return "B1/2" # Текущий игрок проиграет следующему 1 или 2 ходом


for s in range(1, 56):
    if f(s) == "P2":
        print(s)

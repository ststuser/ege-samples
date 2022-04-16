
def steps(n: tuple):
    x, y = n
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)


def f(n: tuple):
    if sum(n) >= 77:
        return "W"
    results = [f(x) for x in steps(n)]
    if any(x == 'W' for x in results):
        return "P1" # Игрок с текущей комбинацией обязательно выиграет первым ходом
    if all(x == "P1" for x in results):
        return "B1" # Игрок с текущей комбинацией обязательно проиграет
    if all(x == "B1" for x in results):
        return "P2" # Игрок с текущей комбинацией обязательно выиграет вторым ходом
    if all(x == "W" or x == 'P2' for x in results):
        return "B1/2" # Игрок с текущей комбинацией обязательно проиграет, при этом второй игрок выиграет 1 или 2 ходом


for s in range(10, 70):
    n = (10, s)
    if f(n) == 'B1':
        print(s)
        break


result = []
for n in range(1, 100, 2):
    for m in range(0, 100, 2):
        N = 2**m * 3**n
        if N <= 600000000 and N >= 400000000:
            result.append(N)

# Сортировка
result.sort()
# Убираю повторяющиеся элементы
result = list(set(result))
print(result)

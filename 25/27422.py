from math import sqrt

# Iterate through all required numbers. Notice that stop in range must be 174506 to include 174505
for number in range(174457, 174506):
    # Create list, that will contain current number dividers. The place to put this call is very important!
    dividers = []
    # Iterate through a square root of possible dividers.
    # Такой полный перебор возможен, поскольку у каждого делителя есть парный делитель.
    # number / divider = mirror_divider
    # Соответственно нет смысла перебирать все числа от 1 до number, поскольку один из парных делителей всегда
    # меньше корня из number.
    # Также не смотрим на 1, поскольку очевидна делимость любого числа на себя и на единицу, кроме того
    # в данной задаче эти делители считать не надо.
    for divider in range(2, int(sqrt(number)) + 1):
        if number % divider == 0:
            dividers.append(divider)
            # При вычислении парного делителя используем целочисленное деление, поскольку необходимо работать с целыми числами.
            # Пы. сы. сравнение int и float может работать корректно. Но вычисление с float могут давать баги в виде
            # +- 0.000000001 к значению, из-за чего всё может сломаться. Поэтому безопаснее по возможности использовать
            # целые числа.
            mirror_divider = number // divider
            # Проверяем что парный делитель не равен исходному.
            if mirror_divider != divider:
                dividers.append(mirror_divider)
    # Print dividers according to task condition
    if len(dividers) == 2:
        print(*dividers)

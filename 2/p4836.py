print('w', 'y', 'z', 'x', 'f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            # for w in range(2):
            f = not (x == (y <= z))
            # if not f:
            print( y, z, x, f)
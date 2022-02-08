from itertools import product

cmb = list(product("ЕГЭ", repeat=5))

cmb = [list(c) for c in cmb]


def is_right(comb) -> bool:
	if comb[0] not in "ЕЭ":
		return False
	return True


result = []
for c in cmb:
	if is_right(c):
		result.append(c)

print(len(result))

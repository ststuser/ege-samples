
text = open('24-s1.txt').read()
stings = text.split('\n')


max_q = 0
string_q = ""

for s in stings:
    q = s.count("Q")
    if q >= max_q:
        max_q = q
        string_q = s

d = {}

for symb in string_q:
    if symb in d:
        d[symb] += 1
    else:
        d[symb] = 1

min_count = 10000
min_alpha = ""

for symb in d:
    if d[symb] < min_count:
        min_count = d[symb]
        min_alpha = symb
    elif d[symb] == min_count and symb < min_alpha:
        min_alpha = symb


print(min_alpha, text.count(min_alpha))

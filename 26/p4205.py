text = open("p4205.txt").read().split("\n")
n, m = text[0].split()
m = int(m)

k_l = [int(x) for x in text[1:] if x]

total_len = sum(k_l)

svar = 0
total_ceil = 0

while sum(k_l) >= m:
    curr = 0
    k_l.sort(reverse=True)
    k_l_copy = k_l[:]
    for i in range(len(k_l_copy)):
        if curr == m:
            break
        if curr + k_l_copy[i] <= m:
            if curr != 0:
                svar += 1
            curr += k_l_copy[i]
            k_l.remove(k_l_copy[i])
        else:
            if i != len(k_l_copy) - 1 and curr + k_l_copy[i+1] >= m:
                continue
            else:
                svar += 1
                curr += k_l_copy[i]
                k_l.remove(k_l_copy[i])
                k_l.append(curr - m)
                break


print(svar, len(k_l))



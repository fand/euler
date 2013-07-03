# -*- coding: utf-8 -*-


import itertools

def t2s(t):
    s = ""
    for c in t:
        s += str(c)
    return s


nines = (t2s(x) for x in itertools.permutations(range(1, 10)))

ans = set()

# num of digits
digits = 9

# x * y = z
for n in nines:
    for digit_x in range(1, 8):
        for digit_y in range(1, digits - digit_x):
            x = n[:digit_x]
            y = n[digit_x : digit_x + digit_y]
            z = n[digit_x + digit_y:]
            if int(x) * int(y) == int(z):
                ans.add(int(z))


print sum(ans)

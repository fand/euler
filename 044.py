import itertools

pentagonals = [(n * (3*n - 1) / 2) for n in range(1, 1001)]
# pentagonals = [(n * (3*n - 1) / 2) for n in range(1, 11)]



d_min = 100000
for c in itertools.combinations(pentagonals, 2):
    if abs(c[0] - c[1]) in pentagonals and abs(c[0] + c[1]) in pentagonals:
        d_min = min(abs(c[0] - c[1]), d_min)

print d_min


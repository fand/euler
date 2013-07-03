
def solutions(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n-a):
            c = n - a - b
            if c > a + b:
                continue
            if a*a + b*b == c*c:
                print a,b,c
                count += 1
    return count



n_max = 0
s_max = 0
for n in range(1, 1001):
    s = solutions(n)
    print "%d: %d solutions" % (n, s)
    if s > s_max:
        s_max = s
        n_max = n

print n_max

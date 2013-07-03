
with open("penta_7.txt", "r") as f:
    pentagonals = [int(x) for x in f.readlines()]

#pentagonals = [(n * (3*n - 1) / 2) for n in range(1, 10000001)]
# pentagonals = [(n * (3*n - 1) / 2) for n in range(1, 11)]


print "reading done!"

d_min = 100000
for n in range(10000, 100000):
    sa = 3*n + 2
    wa = 3*n*n + 2*n + 2
    if sa in pentagonals and wa in pentagonals:
        d_min = min(sa, d_min)
    if n % 1000 == 0:
        print n
        
print "dmin: ", d_min


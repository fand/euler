import pprint as pp

counts = {}
digits = {}

for i in range(2, 1000):
    q = 1
    s = ""
    while len(s) < 1000:
        if (q / i) == 0:
            q *= 10
        else:
            s += str(q / i)
            q = q % i
        if q == 0:
            break
    if q != 0:
        digits[i] = s


for n, d in digits.items():

    for i in range(1, n):
        rep = len(d) / i
        for j in range(i):            
            if d[j:i] * rep == d[j:(i-j)*rep]:
                counts[n] = max(i, counts)
            break

m = 0
ans = 0
for k, v in counts.iteritems():
    if v > m:
        m = v
        ans = k
        
print ans
print digits[ans]
# pp.pprint(counts)
# pp.pprint(digits)

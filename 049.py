import itertools

with open("prime_9.txt", "r") as f:
    primes = [x[:-1] for x in f.readlines()]

print "read"
print primes[0]
print primes[1]
    

for i in range(1000, 10001):
    s = str(i)
    ans = set()
    for perm in itertools.permutations(s, 4):
        ss = reduce(lambda x,y: x+y, perm)
        # ss = ""
        # for c in perm:
        #     ss += str(c)
            
        if ss in primes:
            ans.add(ss)

    if len(ans) > 2:
        ans.sort()
        for i in range(len(ans) - 2)
        ppp = [int(x) for x in sorted(pp)]
        if ppp[2] - ppp[1] == ppp[1] - ppp[0]:
            print ppp

        

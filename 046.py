import copy


primes = []


with open('prime_9.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        primes.append(int(l[:-1]))


ans = copy.copy(primes)

print "reading done!"

for i in range(10000):
    n = 2 * i * i
    for p in primes:
        if p + n in ans:
            ans.remove(p)

    
print "got intersection!"
print ans

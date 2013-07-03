
def factors(num, primes):
    n = num
    s = set()
    size = len(primes)
    i = 0
    while True:
        p = primes[i]
        tmp = 1
        while n % p == 0:
            n /= p
            tmp *= p
        if tmp != 1:
            s.add(tmp)
        if n == 1:
            break
        else:
            i += 1
    return s


    
def is_distinct(sets, s, n):

    if len(s) != n:
        return False
        
    for ss in sets:
        if len(ss) != n:
            return False
        for x in s:
            if x in ss:
                return False
                
    return True

    

with open("prime_9.txt") as f:
    primes = [int(x) for x in f.readlines()]


print "read!"


sets = []
n1 = n2 = 0


sets.append(factors(2, primes))
n1 = 2

count = 0

for i in range(3, 10000000):

    s = factors(i, primes)
    
    if is_distinct(sets, s, 4):
        sets.append(s)
        
    else:
        sets = [s]

        
    if len(sets) == 4:
        print i - 3
        break
        

print "done"


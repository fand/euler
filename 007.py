
primes = [2,3]

i = 6
while i < 2000000:
    l = i - 1
    r = i + 1

    lp = True
    rp = True

    for p in primes:
        if l % p == 0:
            lp = False
        if r % p == 0:
            rp = False

    if lp:
        primes.append(l)
    if rp:
        primes.append(r)

    i += 6

    
print sum(primes)

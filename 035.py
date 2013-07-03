
# do not give num < 4!!!
def is_prime(num, primes):
    # if num < 2:
    #     return False
    # if num == 2 or num == 3:
    #     return True
    for p in primes:
        if p*p > num:
            return True
        if num % p == 0:
            return False
    return True


def get_prime(num):
    primes = [2,3]
    i = 6
    while i < num:
        if is_prime(i-1, primes):
            primes.append(i-1)
        if is_prime(i+1, primes):
            primes.append(i+1)
        i += 6
    return primes


def is_circular(num, primes):
    s = str(num)
    for i in range(1, len(s)):
        if not int(s[i:] + s[:i]) in primes:
            return False
    return True

    
primes = get_prime(1000000)
circ = filter(lambda x: is_circular(x, primes), primes)
print circ
print len(circ)


    

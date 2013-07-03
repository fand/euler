
primes = [2,3,5,7,11,13,17,19,23,29,31]

i = 36
while len(primes) < 10001:
    left = i-1
    right = i+1

    left_prime = True
    right_prime = True
    for p in primes:
        if left % p == 0:
            left_prime = False
        if right % p == 0:
            right_prime = False
    if left_prime:
        primes.append(left)
    if right_prime:
        primes.append(right)
    i += 6



print primes[10000]    

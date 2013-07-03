

def is_truncatable(num, can):
    s = str(num)

    for i in range(len(s)-1):
        if not int(s[:-i-1]) in can:
            return False
        if not int(s[i+1:]) in can:
            return False
    return True


with open("prime_1000000.txt", "r") as f:
    primes = [int(x) for x in f.readlines()]


trunk = []
for p in primes:
    if is_truncatable(p, primes):
        trunk.append(p)
        if len(trunk) == 16:
            break

print trunk
print sum(trunk)

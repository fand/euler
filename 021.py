def divisor(num):
    l = []
    for i in range(1, num/2+1):
        if num % i == 0:
            l.append(i)
    return l


def d(num):
    return sum(divisor(num))


def isAmicable(num):
    dn = d(num)
    if d(dn) == num and num != dn:
        return True
    else:
        return False
        

amic = []    
for i in range(1, 10001):
    if isAmicable(i):
        amic.append(i)


print sum(amic)

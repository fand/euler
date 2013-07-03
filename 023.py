def divisor(num):
    l = []
    for i in range(1, num/2+1):
        if num % i == 0:
            l.append(i)
    return l


def isAbundant(num):
    return True if sum(divisor(num)) > num else False
    



abundant = []
can = []

for i in range(1, 28124):
    if isAbundant(i):
        abundant.append(i)

    for n in abundant:
        if (i - n) in abundant:
            can.append(i)
            break

            
print sum(range(1, 28124)) - sum(can)          
    

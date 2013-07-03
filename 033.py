import itertools

def lcm(n, m):
    tn, tm = n, m
    
    while tn != tm:
        if tn > tm:
            tm += m
        else:
            tn += n

    return tn

nomin = []
denom = []    

for i in range(1, 10):
    for a in range(1, 10):
        for b in range(1, 10):
            # candidates are:
            # 10a + i / 10b + i
            # 10i + a / 10b + i
            # 10a + i / 10i + b
            # 10i + a / 10i + b
            if (10*a + i) < (10*b + i) and (10*a + i) * b == (10*b + i) * a:
                nomin.append(10*a + i)
                denom.append(10*b + i)
            if (10*i + a) < (10*b + i) and (10*i + a) * b == (10*b + i) * a:
                nomin.append(10*i + a)                
                denom.append(10*b + i)
            if (10*a + i) < (10*i + b) and (10*a + i) * b == (10*i + b) * a:
                nomin.append(10*a + i)
                denom.append(10*i + b)
            if (10*i + a) < (10*i + b) and (10*i + a) * b == (10*i + b) * a:
                nomin.append(10*i + a)
                denom.append(10*i + b)

print nomin
print denom

print reduce(lambda x,y: x*y, nomin)
print reduce(lambda x,y: x*y, denom)
#print reduce(lcm, denom)




def lpf(num):
    l = []
    n = num
    i = 2

    while True:
        if n % i == 0:
            l.append(i)
            n = n/i
            i = 2
            if n == 1:
                break
            continue
        else:
            i += 1
            
    
    return l

    

q = 600851475143
print lpf(q)


def tri(n):
    return n*(n+1)/2

def penta(n):
    return n*(3*n - 1)/2
    
def hexa(n):
    return n*(2*n - 1)

    
t = 285
p = 165
h = 143

t += 1

tt = tri(t)
pp = penta(p)
hh = hexa(h)


while True:
    if tt == pp == hh:
        break
    if tt < pp and tt < hh:
        t += 1
        tt = tri(t)
    if pp < tt and pp < hh:
        p += 1
        pp = penta(p)
    if hh < tt and hh < pp:
        h += 1
        hh = hexa(hh)
    
print tt

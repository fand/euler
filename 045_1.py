
t = set()
p = set()
h = set()


with open('tri_7.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        t.add(l)
        
with open('pen_7.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        p.add(l)
        
with open('hex_7.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        h.add(l)


print "reading done!"

u = (t.intersection(p)).intersection(h)

print "got intersection!"
print u

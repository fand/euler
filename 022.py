def score(name):
    s = 0
    for c in name:
        s += ord(c) - ord('A') + 1
    return s
    

with open("names.txt") as f:
    names = [x[1:-1] for x in f.read().split(',')]

names.sort()
    
print sum([score(n)*(i+1) for i,n in enumerate(names)])

import pprint as pp

lattice = []
for i in range(21):
    lattice.append([1] * 21)
    
pp.pprint(lattice)
    
for y in range(1,21):
    for x in range(1, 21):
        lattice[y][x] = lattice[y-1][x] + lattice[y][x-1]
    

pp.pprint(lattice)

with open("triangle.txt", "r") as f:
    lines = f.readlines()


tree = []

for ls in lines:
    tree.append( [int(x) for x in ls.split(' ')] )

    

depth = len(tree) - 2
while depth >= 0:
    column = tree[depth]

    for i in range(len(tree[depth])):
        tree[depth][i] += max(tree[depth+1][i], tree[depth+1][i+1])

    depth -= 1


print tree[0]

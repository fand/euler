import pprint as pp

l = [0] * 1001
for i in range(1001):
    l[i] = [0] * 1001


x = 500
y = 500

l[x][y] = 1
x += 1
count = 2
s = 1

for i in range(1, 501):
    width = i * 2 + 1
    #print "x: %d, y: %d" % (x, y)

    try:
        # r bottom
        for j in range(width - 1):
            l[x][y] = count
            y += 1
            count += 1
        x -= 1
        y -= 1
        s += count-1
            
        # l bottom
        for j in range(width - 1):
            l[x][y] = count
            x -= 1
            count += 1
        x += 1
        y -= 1
        s += count-1

        # l top
        for j in range(width - 1):
            l[x][y] = count
            y -= 1
            count += 1
        x += 1
        y += 1
        s += count-1

        # r top
        for j in range(width - 1):
            l[x][y] = count
            x += 1
            count += 1
        s += count-1
        
    except:
        print x, y

#pp.pprint(l)
print s


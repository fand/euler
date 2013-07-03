coins = [1, 2, 5, 10, 20, 50, 100, 200]
maxes = {1:200, 2:100, 5:40, 10:20, 20:10, 50:4, 100:2, 200:1}

count = 0

for a in range(201):
    for b in range(101):
        for c in range(41):
            for d in range(21):
                for e in range(11):
                    for f in range(5):
                        for g in range(3):
                            for h in range(2):
                                p = 1*a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h
                                if p == 200:
                                    count += 1
    
print count


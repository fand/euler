

f1 = 1
f2 = 1
count = 2

while True:
    tmp = f1 + f2
    f1 = f2
    f2 = tmp
    count += 1

    
    s = str(f2)
    if len(s) == 1000:
        break

print count       
    

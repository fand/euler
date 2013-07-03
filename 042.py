def wordnum(s):
    base = ord('A') - 1
    return sum([ord(c)-base for c in s])


triangles = []
for i in range(1, 300):
    triangles.append(i * (i + 1) / 2)


with open("words.txt", "r") as f:
    words = [x[1:-1] for x in f.read().split(',')]

    
count = 0

for w in words:
    if wordnum(w) in triangles:
        count += 1

print count        

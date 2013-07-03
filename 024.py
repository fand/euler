import copy



def serialize(l):
    s = ""
    for n in l:
        s += str(n)
    return s




perm = []
ans = []

def permutate(n, m):
    if n == m:
        ans.append(serialize(perm))
    for x in range(0, n):
        if x in perm: continue
        perm.append(x)
        permutate(n, m+1)
        perm.pop()


permutate(10, 0)
print ans[1000000-1]

# permutate(3, 0)
# print ans


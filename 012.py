
def getDivisors(num):
    ans = []
    for i in range(1, num/2 + 1):
        if num % i == 0:
            ans.append(i)
    return ans


t = 0
count = 1

while True:
    t += count
    count += 1

    if len(getDivisors(t)) > 500:
        print t
        exit()


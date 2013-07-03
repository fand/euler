


days_normal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
days_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]


def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False




def dpy(year):
    return 366 if is_leap(year) else 365
    

count = 0
off = 1
for year in range(1901, 2001):
    days = days_leap if is_leap(year) else days_normal
    acc = 0
    for d in days:
        if (d + acc + off) % 7 == 6:
            count += 1
        acc += d
            
    t = off + dpy(year)
    
    off = 0 if t % 7 == 0 else t % 7
    

print count






def is_power(num, power):
    s = str(num)
    if num == sum([pow(int(c), power) for c in s]):
        return True
    else:
        return False


        
# candidates must be less than (9**5) * 5
lim = pow(9,5) * 5
print sum(filter(lambda x: is_power(x, 5), range(2,lim)))

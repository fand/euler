def factorial(num):
    return 1 if num == 1 else num * factorial(num - 1)



print sum([int(x) for x in str(factorial(100))])

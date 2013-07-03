
def factorial(num):
    return 1 if num <= 1 else num * factorial(num-1)

facts = [factorial(n) for n in range(10)]
    
# find biggest candidate
nine = factorial(9)
digit = 1
while int('9' * digit) < nine * digit:
    digit += 1

print facts

ans = []
for i in range(3, pow(10, digit)):
    if i == sum([facts[int(c)] for c in str(i)]):
        ans.append(i)

print ans        
print sum(ans)        
    

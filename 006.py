for c in range(1,999):
    for b in range(1,999-c):
        a = 1000 - b - c

        if a*a + b*b == c*c and a < b < c:
            print a * b * c
            
        

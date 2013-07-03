

def is_palindrome(num):
    if is_palindrome_dec(num) and is_palindrome_bin(num):
        return True
    return False
    

def is_palindrome_dec(num):
    s = str(num)
    lim = len(s)/2  # Note: digit at center doesn't need inspection.
    for i in range(lim):
        if s[i] != s[-1-i]:
            return False
    return True


def is_palindrome_bin(num):
    s = bin(num)[2:]
    lim = len(s)/2  # Note: digit at center doesn't need inspection.
    for i in range(lim):
        if s[i] != s[-1-i]:
            return False
    return True
    


s = 0    
for i in range(1000000):
    s += i if is_palindrome(i) else 0
print s

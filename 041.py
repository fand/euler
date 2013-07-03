
class Pan:

    def __init__(self, digit):
        self.buf = {}
        for i in range(1, digit+1):
            self.buf[str(i)] = 0


    def clear(self):
        for k in self.buf:
            self.buf[k] = 0
            
    def is_pan(self, num):
        self.clear()
        for c in num:
            if c == '0':
                return False
            self.buf[c] += 1

        for k, v in self.buf.items():
            if v != 1:
                return False
                
        return True
    



with open("prime_1000000.txt", "r") as f:
    primes = [x.rstrip() for x in f.readlines()]


pans = [None, Pan(1), Pan(2), Pan(3), Pan(4), Pan(5), Pan(6), Pan(7), Pan(8), Pan(9)]
    
for n in primes:
    i = len(n)
    p = pans[i]
    if p.is_pan(n):
        print n


s_1d = { "1": "one",
         "2": "two",
         "3": "three",
         "4": "four",
         "5": "five",       
         "6": "six",
         "7": "seven",
         "8": "eight",       
         "9": "nine" }

s_teen = { "11": "eleven",
           "12": "twelve",
           "13": "thirteen",
           "14": "fourteen",
           "15": "fifteen",
           "16": "sixteen",
           "17": "seventeen",
           "18": "eighteen",
           "19": "nineteen" }

s_2d = { "1": "ten",
         "2": "twenty",
         "3": "thirty",
         "4": "forty",
         "5": "fifty",       
         "6": "sixty",
         "7": "seventy",
         "8": "eighty",       
         "9": "ninety" }


def d2s(s):
    return s_1d[s]


def dd2s(s):
    if s[0] == '0':
        return s_1d[s[1]]
    elif s[1] == '0':
        return s_2d[s[0]]
    elif s[0] == '1':
        return s_teen[s]
    else:
        return s_2d[s[0]] + s_1d[s[1]]

        
def ddd2s(s):
    if s[1:] == "00":
        return s_1d[s[0]] + "hundred"
    return s_1d[s[0]] + "hundred" + "and" + dd2s(s[1:])




ans = ""
for i in range(1000):
    src = str(i+1)
    s = ""
    
    if len(src) == 1:
        s += d2s(src)
    elif len(src) == 2:
        s += dd2s(src)
    elif len(src) == 3:
        s += ddd2s(src)
    else:
        s += "one" + "thousand"
            
    print s
    ans += s


        

print len(ans)    

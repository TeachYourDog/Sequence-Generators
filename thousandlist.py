import time

ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]

twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]

thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "]


def num999(n):
    c = int(n % 10) # singles digit
    b = int(((n % 100) - c) / 10) # tens digit
    a = int(((n % 1000) - (b * 10) - c) / 100) # hundreds digit
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[a] + "hundred "
    elif a != 0:
        t = ones[a] + "hundred and "
    if b <= 1:
        h = ones[n%100]
    elif b > 1:
        h = twenties[b] + ones[c]
    st = t + h
    return st

def num2word(num):
    i = 3
    n = str(num)
    word = ""
    k = 0
    while(i == 3):
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
                word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word
        if n == '':
            i = i+1
        k += 1
    return word[:-1]

file1=open("thousandnumber","w")
for i in range(1,1001):
    num=i
    print(num2word(i))
    file1.write(num2word(i))
    file1.write("\n")
    i=i+1

file1.close()

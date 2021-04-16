
def collatz(a,numlist):
    
    while a != 1:
        if a%2 == 0:
            a = a / 2
            print(a)
            numlist.append(a)
        else:
            a = 3*a + 1
            print(a)
            numlist.append(a)


a = input("What is the first number?")
a = int(a)

numlist = [a]

print(a)
collatz(a,numlist)
print(len(numlist))

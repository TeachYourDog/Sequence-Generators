





def collatz(a):
    while a != 1:
        if a%2 == 0:
            a = a / 2
            print(a)
        else:
            a = 3*a + 1
            print(a)


collatz(2)

i = 1
x = 100

nbprime = 0
while True:
    c=0;
    for j in range(1, (i+1)):
        a = i%j
        if (a==0):
            c = c+1
    if (c==2):
        print(nbprime,',', i)
        nbprime = nbprime + 1
        if nbprime >= x:
            break
    i=i+1
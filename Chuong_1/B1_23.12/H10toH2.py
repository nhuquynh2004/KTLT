def H10ToH2(n):
    if n>0:
        sd=n%2
        n=n//2
        H10ToH2(n)
        print(sd,end='')
n=31
print(f'Số nhị phân của {n}= ',end='')
H10ToH2(n)
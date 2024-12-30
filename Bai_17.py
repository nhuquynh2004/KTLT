def H10ToH16(n):
    if n>0:
        sd=n%16
        n=n//16
        H10ToH16(n)
        if sd==10: so = 'A'
        elif sd==11: so = 'B'
        elif sd==12: so = 'C'
        elif sd==13: so = 'D'
        elif sd==14: so = 'E'
        elif sd==15: so = 'F'
        else: so = str(sd)
        print(so,end='')
n=317547
print(f'Số thập lục phân của số {n}= ')
H10ToH16(n)
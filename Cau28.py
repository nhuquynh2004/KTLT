s='5;7;8;-2;8;11;13;9;10'
s=input('s=')
taphop=s.split(';')
def splitstr():
    for i in taphop: print(i)
def analysis():
    even=0
    isEven=[]
    negative=0
    isNegative=[]
    prinum=0
    isPrimenum=[]
    for i in taphop:
        n=int(i)
        if n%2==0: 
            even=even+1
            isEven.append(n)
        if n<0: 
            negative=negative+1
            isNegative.append(n)
        if isPrime(n)==True: 
            prinum=prinum+1
            isPrimenum.append(n)
    print(f'Có {even} số chẵn, bao gồm {isEven}')
    print(f'Có {negative} số âm, bao gồm {isNegative}')
    print(f'Có {prinum} số nguyên tố, bao gồm {isPrimenum}')
def isPrime(n):
    if n<1: 
        return False
    else:
        for i in range (2,n//2+1):
            if n%i==0: 
                return False
                break
        return True
def average():
    aver=0
    for i in taphop:
        n=int(i)
        aver=aver+n
    aver=aver/(len(taphop))
    print(f'Giá trị trung bình = {aver}')

splitstr()
analysis()
average()

    
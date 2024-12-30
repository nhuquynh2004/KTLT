def handle(f,x):
    return f(x)
#cách 1: Thử ra lệnh lambda làm hàm ktr số lẻ
ret1=handle(lambda x: x%2!=0, 8)
print('ret1=',ret1)
#cách 2: viết tường minh ra 
def isOdd(n):
    return n%2!=0
ret2 = isOdd(7)
ret3 = handle(lambda x: isOdd(x), 7)
print('ret2=',ret2)
print('ret3=',ret3)

def giaithua(n):
    gt = 1
    for i in range (1,n+1):
        gt=gt*i
    return gt
ret4=handle(lambda x: giaithua(x),5)
print('5!=',ret4)

def handle2(f,x,y):
    return(f(x,y))
ret5=handle2(lambda x,y: x+y, 5, 3)
print(ret5)
def giaithua(n):
    gt = 1
    for i in range (1,n+1):
        gt=gt*i
    return gt

gt_5=giaithua(5)
print('5!=',gt_5)

def P(n,k):
    return giaithua(n)//giaithua(n-k)

def C(n,k):
    return giaithua(n)//(giaithua(n-k)*giaithua(k))

print('5P3=',P(5,3))
print('5C3=',C(5,3))
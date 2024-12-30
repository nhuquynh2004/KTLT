def fib(n):
    if n<=2: return 1
    return fib(n-1) + fib(n-2)
def list_fib(n):
    for i in range (1,n+1):
        f=fib(i)
        print(f,end=' ')
n=10
list_fib(n)
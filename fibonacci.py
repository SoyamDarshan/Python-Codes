fi=[None]*11
def fib(n):
    if(n==0 or n==1):
        fi[n] = n
    if fi[n] is None:
        fi[n] = fib(n-1)+fib(n-2)
    return fi[n]

        
f=fib(10)
print fi        
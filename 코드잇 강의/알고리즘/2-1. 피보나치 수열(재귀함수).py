def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

for i in range(1, 11):
    print(fib(i))
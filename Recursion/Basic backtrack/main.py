def f(i,n):
    if n < i:
        f(i,n+1)
    print(n)


i = int(input())
f(i,1)
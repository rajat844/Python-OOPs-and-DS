def f(n,sum):
    if n < 1:
        print(sum)
        return
    sum += n
    f(n-1,sum)

n = int(input())
sum = 0
f(n,sum)
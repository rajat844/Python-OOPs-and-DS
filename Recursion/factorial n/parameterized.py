def f(n,product):
    if n < 2:
        print(product)
        return
    product *= n
    f(n-1,product)

n = int(input())
product = 1
f(n,product)
x = int(input("enter the number: "))
n = int(input("enter the precision: "))


# def taylor(x, n):
#     ans = 1
#     for i in range(n, 0,-1):
#         ans = 1+x/i * ans
#     return ans
ans = 1
def taylor(x,n):
    global ans
    if(n == 0):
        return ans
    ans = 1+x/n * ans
    return taylor(x,n-1)


print(taylor(x, n))

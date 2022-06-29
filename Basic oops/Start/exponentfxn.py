# def exponent(x,n):
#     if(x==0 or x==1):
#         return 1
#     if(n==0):
#         return 1
    
#     if(n%2 == 0):
#         return (exponent(x*x,n/2))
#     else:
#         return  (x*exponent(x*x,(n-1)/2))

def exponent(x,n):
    result  = 1
    for i in range(n):
        result = result *x
    return result



x= int(input())
n = int(input())

ans = exponent(x,n)
print(ans)
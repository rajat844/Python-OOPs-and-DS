n = int(input("Enter the number: "))

# def fibonacci(n):
#     if(n<=1):
#         return n
#     a1 = 0
#     a2 = 1
#     s = 0

#     for i in range(2,n+1):
#         s = a1 + a2
#         a1 = a2
#         a2 = s
#     return a2

# def fibonacci(n):
#     if(n<=1):
#         return n
#     else :
#         return (fibonacci(n-1) + fibonacci(n-2))

arr = [-1]*(n+1)

def fibonacci(n):
    if(n <= 1):
        arr[n] = n
        return n
    else:
        if(arr[n] == -1):
            t = fibonacci(n-1)+fibonacci(n-2)
            arr[n] = t
            return t
        else:
            return arr[n]

print(fibonacci(n))

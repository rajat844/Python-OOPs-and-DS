def sumOfN(n):
    if(n == 0):
        return 0
    else:
        return (sumOfN(n-1) + n)

n = int(input("Enter the Number: "))
print(sumOfN(n))

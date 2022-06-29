def pow(n, m):
    if(n == 0):
        return 1
    if(m == 0 or m == 1):
        return 1
    if(n%2 == 1):
        return (m* pow((n-1)/2,m*m))
    else :
        return (pow(n/2,m*m))


m = int(input("Enter the number: "))
n = int(input("Enter the power: "))

print(pow(n, m))

# pascals triangle

n = int(input("Enter the n:"))
r = int(input("Enter the r :"))


def nCr(n, r):
    if(n == r or r == 0):
        return 1
    else:
        return (nCr(n-1, r-1) + nCr(n-1, r))


print(nCr(n, r))

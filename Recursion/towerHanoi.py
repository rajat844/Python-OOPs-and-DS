n = int(input("No of towers: "))
A = 1
B = 2
C = 3


def TOH(n, A, B, C):
    if n > 0:
        TOH(n-1, A, C, B)
        print(A,C)
        TOH(n-1, B, A, C)


print(TOH(n, A, B, C))

def cube(num):
    if(num >=1):
        return (cube(num-1) + num)
    else:
        return 0

i = int(input())
result = cube(i)
print(result)
def taylorSeries(x, y):
    r = 0
    if(x == 0):
        return 1
    if(y == 0):
        return 1
    else:
        r = taylorSeries(x, y-1)
        taylorSeries.p = taylorSeries.p * x
        taylorSeries.f = taylorSeries.f * y
        return (r+(taylorSeries.p/taylorSeries.f))

taylorSeries.p = 1
taylorSeries.f = 1

x = int(input("Enter the number: "))
y = int(input("Enter the presition: "))

print(taylorSeries(x, y))

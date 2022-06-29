num = [1,2,3,4,5,6,7]
numGrid = [
    [1,2,3],
    [5,6,7],
    [4,6,9],
    [0]
]

print(numGrid[2][2])

for i in range(len(numGrid)):
    for j in range(len(numGrid[i])):
        print(numGrid[i][j])
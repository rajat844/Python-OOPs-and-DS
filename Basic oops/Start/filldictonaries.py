arr1 = [["A","1dec",10],["B","2dec",15],["C","3dec",20],["A","4dec",15]]

ans = {}

for i in range(len(arr1)):
    ans[arr1[i][0]] = [arr1[i][1],arr1[i][2]]

print(ans)
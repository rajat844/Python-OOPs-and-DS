from re import S


def allSubsequeces(string):
    ans = []
    n = len(string)

    def helper(s,index):
        if index == n:
            new = s
            ans.append(new)
            return 
        s += string[index]
        helper(s,index+1)
        s = s[:-1]
        helper(s,index+1)
    helper("",0)
    return ans

string = input()
x = allSubsequeces(string)
print(x)
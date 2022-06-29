import sys
from collections import defaultdict

dic = defaultdict(int)

try:
    for line in sys.stdin:
        x, y = line.rstrip().split('=')
        y = int(y)
        dic[x] = y
except:
    dict(sorted(dic.items(), key=lambda x: x[1]))

for x in dic:
    print(x, "=", dic[x])


# charles=3918
# alice=0
# bob=100
# charles=3918
# django=77
# alice=0
# foo=10
# bar=10
# bob=50

from collections import defaultdict, deque


def bfs(p, q, n):
    adj = defaultdict(list)
    for i in range(len(p)):
        adj[p[i]].append(q[i])
        adj[q[i]].append(p[i])

    bfslist = []
    vis = [False] * (n)
    for i in range(1, n+1, 1):
        if vis[i-1] == False:
            q = deque()
            q.append(i)
            vis[i-1] = True
            while len(q) > 0:
                node = q.popleft()
                bfslist.append(node)

                for j in adj[node]:
                    if vis[j-1] == False:
                        q.append(j)
                        vis[j-1] = True

    return bfslist


def dfs(p, q, n):
    adj = defaultdict(list)
    for i in range(len(p)):
        adj[p[i]].append(q[i])
        adj[q[i]].append(p[i])

    def dfshelper(x):
        nonlocal dfslist
        dfslist.append(x)
        vis[x-1] = True
        for i in adj[x]:
            if vis[i-1] == False:
                dfshelper(i)

    vis = [False] * n
    dfslist = []

    for i in range(1, n+1, 1):
        if vis[i-1] == False:
            dfshelper(i)

    return dfslist

p = list(map(int, input().strip().split()))
q = list(map(int, input().strip().split()))
n = int(input())
print(bfs(p, q, n))
print(dfs(p, q, n))

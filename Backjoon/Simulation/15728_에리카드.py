N,K = map(int,input().split())
share = list(map(int,input().split()))
team = list(map(int,input().split()))

for _ in range(K):
    s = -1000000000000
    x = 0
    for i in team:
        for j in share:
            if s <= i*j:
                s = i*j
                x = i
    team.remove(x)
ans = -1000000000000
for i in team:
    for j in share:
        ans = max(ans, i*j)
print(ans)
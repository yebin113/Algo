

N,M = map(int,input().split())
trains = [[0]*20for _ in range(N)]

for _ in range(M):
    orders = list(map(int,input().split()))
    # print(orders)
    order = orders.pop(0)
    if order == 1:
        train, seat = orders[0] -1,orders[1] -1
        trains[train][seat]=1
    elif order == 2:
        train, seat = orders[0] -1,orders[1] -1
        trains[train][seat] = 0
    elif order == 3:
        train = orders[0] -1
        trains[train].insert(0,0)
        trains[train].pop()

    elif order == 4:
        train = orders[0] -1
        trains[train].append(0)
        trains[train].pop(0)


    # for i in range(N):
    #     print(trains[i])
    # print()
visited = []
for i in range(N):
    if trains[i] not in visited:
        visited.append(trains[i])
    # print(visited)
print(len(visited))
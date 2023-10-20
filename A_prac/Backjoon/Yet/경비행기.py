def dis_to_oil(sti, stj, edi, edj):
    km = ((sti - edi) ** (2) + (stj - edj) ** (2)) ** (1 / 2)
    if km % 10:
        return int(km // 10 + 1)
    else:
        return int(km // 10)


import sys

input = sys.stdin.readline

N, K = map(int, input().split())
oil_station = [[0, 0]] * N
for i in range(N):
    x, y = map(int, input().split())
    oil_station[i] = [x, y]

oil_station.sort(key=lambda x:((x[0])**(2)+(x[1])**(2))**(1/2))

start = 1
end = dis_to_oil(0, 0, 10000, 10000)
ans = 0
while start <= end:
    mid = (start + end) // 2
    sti = 0
    stj = 0
    charge = 0
    max_charge = 0
    oil_station[i:] = sorted(oil_station[i:],key=lambda x: ((x[0]-sti) ** (2) + (x[1]-stj) ** (2)) ** (1 / 2))
    for i in range(N):
        oil = dis_to_oil(sti, stj, oil_station[i][0], oil_station[i][1])
        if oil >= mid:
            sti = oil_station[i][0]
            stj = oil_station[i][1]
            oil_station[i:] = sorted(oil_station[i:], key=lambda x: ((x[0] - sti) ** (2) + (x[1] - stj) ** (2)) ** (1 / 2))
            max_charge = max(max_charge, oil)
            charge += 1

    if charge > K:
        start = mid + 1
    else:
        end = mid - 1
        ans = max_charge
print(ans)

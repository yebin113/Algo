N = int(input())
K: int = int(input())
sensor = list(map(int,input().split()))
sensor.sort()

if K>=N:
    print(0)
else:
    dis = []
    for i in range(1,N):
        d = sensor[i] - sensor[i-1]
        dis.append(d)
    dis.sort()
    # print(dis[:N-K])
    print(sum(dis[:N-K]))


    dis.sort(reverse=True)
    for _ in range(K-1):
        dis.pop(0)
    print(dis)

    print(sum(dis))
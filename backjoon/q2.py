

N = int(input())
q = [0]*N
f = 0
r = 0
for i in range(N):
    arr = list(input().split())
    if arr[0] == 'push':
        q[r] = int(arr[1])
        r += 1
    elif arr[0] =='pop':
        if f == r:
            print(-1)
        else:
            print(q[f])
            f += 1
    elif arr[0] =='front':
        if f == r:
            print(-1)
        else:
            print(q[f])
    elif arr[0] =='back':
        if f == r:
            print(-1)
        else:
            print(q[r - 1])
    elif arr[0] =='empty':
        if f == r:
            print(1)
        else:
            print(0)
    elif arr[0] =='size':
        print(r-f)

    # print(f'f:{f} r:{r} q:{q}')
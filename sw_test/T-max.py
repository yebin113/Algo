N = int(input())
arr = []
for i in range(1,N):
    arr.append([0]*i)
for i in range(2*N -1):
    if i % 2 == 1:
        arr.append([0]*(N-1))
    else:
        arr.append([0]*N)
for i in range(N-1,0,-1):
    arr.append([0]*i)
for i in range(4*N-3):
    print(arr[i])

arr[0][0] = 1

dir = {
    # 오른쪽 아래로
    1: [1,1],
    # 그대로 아래로
    2: [2,0],
    # 왼쪽 아래로
    3: [1,-1],
    # 왼쪽 타고 올라오기
    4: [-1,0],
    # 두칸 올라오기
    5: [-2,0],
}
d = 1
length = 1
i = 0
j = 0
num = 1
last = 3* N * (N-1) +1
while 1:
    if num == last:
        break
    num += 1
    di, dj = dir[d]
    ni = i + di
    nj = j + dj
    length = len(arr[i])
    print(ni,nj,d,num)
    try:
        if d == 4 and length != len(arr[ni]):
            d += 1
        if arr[ni][nj] != 0:
            d -= 1
        di, dj = dir[d]
        ni = i + di
        nj = j + dj
        arr[ni][nj] = num
    except:
        d += 1
        d = d % 6
        di, dj = dir[d]
        ni = i + di
        nj = j + dj
        arr[ni][nj] = num
    print(arr)
    i = ni
    j = nj

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')







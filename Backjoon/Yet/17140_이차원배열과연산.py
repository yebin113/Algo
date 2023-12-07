direction = {
    1:[0,1],
    2:[1,0]
}
def cal(arr):
    N = len(arr)
    M = len(arr[0])
    # N이 M보다 같거나 큰 경우 R 연산
    if N >= M:
        max_len = 0
        for i in range(N):
            arr[i] = count_line(arr[i])
            max_len = max(max_len,len(arr[i]))
        # 0추가
        for i in range(N):
            if len(arr[i]) < max_len:
                arr[i] += [0] * (max_len-len(arr[i]))
        # print('R 수행')

    else:
        # 행 열 바꿔서 계산
        arr = rotate(arr)
        max_len = 0
        for i in range(M):
            arr[i] = count_line(arr[i])
            max_len = max(max_len, len(arr[i]))

        # 0추가
        for i in range(M):
            if len(arr[i]) < max_len:
                arr[i] += [0] * (max_len - len(arr[i]))

        arr = rotate(arr)
        # print('C 수행')
    # print(arr)
    if N > 100:
        arr = arr[:100]
    if M > 100:
        arr = rotate(rotate(arr)[:100])
    return arr


def count_line(line):

    set_line = list(set(line))
    cnt = []
    for num in set_line:
        if num == 0:
            continue
        cnt.append([num,line.count(num)])
    cnt.sort(key=lambda x:(x[1],x[0]))
    res = []
    for c in cnt:
        res.extend(c)

    return res

def rotate(arr):
    N = len(arr)
    M = len(arr[0])
    arr2 = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            arr2[i][j] = arr[j][i]
    return arr2

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
while 1:
    # print(cnt,'번째 계산')
    # print(f'r: {r} c: {c} k:{k}')
    # for i in range(len(A)):
    #     print(A[i])
    if len(A) >= r and len(A[0]) >= c:
        # print(A[r-1][c-1], k)
        if A[r-1][c-1] == k:
            print(cnt)
            break
    if cnt > 100:
        print(-1)
        break

    A = cal(A)
    cnt += 1

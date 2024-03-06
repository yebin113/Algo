from collections import deque


def bfs(i, j, color):
    # 주변의 같은 색의 인덱스를 확인후 반환
    q = deque()
    q.append((i, j))
    array = []
    # print(i,j,'검사중 색은',color)
    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if not (0 <= ni < 12 and 0 <= nj < 6) or arr[ni][nj] != color or visited[ni][nj] != 0:
                continue
            q.append((ni, nj))
            array.append((ni, nj))
            visited[ni][nj] = 1
    # print('같은 색 위치',array)
    return array


def turn():

    # 뿌요가 터지는지 확인
    is_pop = False
    for i in range(12):
        for j in range(6):
            # 이미 방문한 곳이면 넘기기
            if visited[i][j] != 0 or arr[i][j] == '.':
                continue
            # 인접한 같은 색의 리스트
            same = bfs(i,j,arr[i][j])
            # 4개 이상이 아니면 아무일도 일어나지 않음
            if len(same) < 4:
                # print('안터짐')
                continue

            is_pop = True
            for si,sj in same:
                arr[si][sj] = '.'
    # print('터진 직후 배열')
    # for i in range(12):
    #     print(arr[i])
    # print()

    # 터진 뒤 밑으로 가라앉기
    for j in range(6):
        now = deque()
        for i in range(11,-1,-1):
            if arr[i][j] != '.':
                now.append(arr[i][j])
                arr[i][j] = '.'
        for i in range(11,-1,-1):
            if len(now) == 0:
                break
            arr[i][j] = now.popleft()
    # print('정리된 배열')
    # for i in range(12):
    #     print(arr[i])
    # print()
    return is_pop


dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
arr = []
cnt = 0
for _ in range(12):
    arr.append(list(input()))

while 1:
    visited = [[0]*6 for _ in range(12)]
    if turn() == False:
        break
    cnt += 1
print(cnt)
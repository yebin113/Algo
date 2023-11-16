def put_sticker_on(sticker,visited):
    n = len(sticker)
    m = len(sticker[0])
    # print('현재 스티커')
    # for i in range(n):
        # print(sticker[i])
    if n > N or m > M:
        # print('안들어가집니다..')
        return False,visited
    is_enter = True
    for i in range(N - n+1):
        for j in range(M - m+1):
            # print(i,j,visited[i][j])
            is_enter = True
            for k in range(n):
                for l in range(m):
                    # print(k,m,sticker[k][l])
                    if visited[k + i][l + j] + sticker[k][l] > 1:
                        is_enter = False
                        break

                if is_enter == False:
                    break
            if is_enter == True:
                for k in range(n):
                    for l in range(m):
                        visited[k+i][l+j] += sticker[k][l]
                break
        if is_enter == True:
            break
    # print(f'스티커 들어가기는? {is_enter}')
    # for i in range(N):
    #     print(visited[i])
    return is_enter,visited


def rotation(sticker):
    n = len(sticker)
    m = len(sticker[0])
    arr = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[j][n-i-1] = sticker[i][j]
    return arr




N,M,K = map(int,input().split())
stickers = []
area = [[0]*M for _ in range(N)]
for _ in range(K):
    r,c = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(r)]
    for x in range(4):
        is_entered,area = put_sticker_on(sticker,area)
        if is_entered:
            break
        sticker = rotation(sticker)

print(sum(sum(area,[])))

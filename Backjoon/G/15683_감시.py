def dfs(step,room):
    global min_blind_spot
    if step == len(camera):
        # 감시지대 표시 다 했으면 사각지대 세기
        blind_spot = 0


        for i in range(N):

            for j in range(M):
                if room[i][j] == 0:
                    blind_spot += 1
        # 사각지대 갱신
        min_blind_spot = min(blind_spot,min_blind_spot)
        # print('최소',min_blind_spot)
        return
    else:
        cam = camera[step][0]
        cami = camera[step][1]
        camj = camera[step][2]

        for dir in range(len(direction[cam])):
            dfs(step+1,connect(cam,cami,camj,dir,room))



import copy
def connect(cam_type,sti,stj,dir,room):
    arr = copy.deepcopy(room)

    # print(f'{sti,stj}위치에 있는 {cam_type}을 {dir}방향으로 연결')
    for di,dj in direction[cam_type][dir]:
        i = sti
        j = stj
        while 0<=i+di<N and 0<=j+dj<M:
            i += di
            j += dj
            if arr[i][j] == 0:
                arr[i][j] = '#'
            elif arr[i][j] == 6:
                break
    # for i in range(N):
    #     print(arr[i])
    return arr



N,M = map(int,input().split())
office = [list(map(int,input().split())) for _ in range(N)]
min_blind_spot = 100000000000000000000000
camera = []
direction = {
    1: [ [[0,1]] , [[1,0]] , [[-1,0]] , [[0,-1]] ],
    2: [ [[0,-1],[0,1]] , [[1,0],[-1,0]] ],
    3: [ [[0,-1],[1,0]] , [[0,-1],[-1,0]], [[0,1],[1,0]], [[0,1],[-1,0]]  ],
    4: [ [[1,0],[-1,0],[0,1]], [[0,-1],[-1,0],[0,1]], [[0,-1],[1,0],[0,1]], [[0,-1],[1,0],[-1,0]] ],
    5: [ [[0,1],[0,-1],[-1,0],[1,0]] ]
}
for i in range(N):
    for j in range(M):
        if office[i][j] in [1,2,3,4]:
            # 카메라 종류와 위치를 저장
            camera.append([office[i][j],i,j])
        # 5번 카메라면 모든방향에 감시 가능함 미리 표시
        elif office[i][j] == 5:
            office = connect(5,i,j,0,office)

dfs(0,office)
print(min_blind_spot)



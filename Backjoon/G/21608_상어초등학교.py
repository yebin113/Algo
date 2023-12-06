
"""
조건에 맞게 학생들을 앉히고 돌아가며 만족도 조사
앉힐때 만족도 조사를 겸하면 미래에 친구가 앉아서 만족도가 높아질
경우를 고려하지 못할거같아서 따로 구현
"""
def insert_student(me,friends):
    # print(f'나는 {me} 내가 좋아하는 학생 {friends}')
    max_around = 0
    max_blank = 0
    mi = 0
    mj = 0
    last = []
    # 모든 칸을 돌아가면서
    for i in range(N):
        for j in range(N):
            # 이미 임자있는 자리면 넘기기
            if my_class[i][j] != 0:
                continue
            last.append((i,j))
            around = 0
            blank = 0
            # 그 주변칸에
            for di, dj in [[0,1],[0,-1],[-1,0],[1,0]]:
                ni = i + di
                nj = j + dj
                if ni < 0 or nj < 0 or ni >= N or nj>= N:
                    continue
                # 내 친구가 있다면 around에 추가해준다
                if my_class[ni][nj] in friends:
                    around += 1
                if my_class[ni][nj] == 0:
                    blank += 1
            # print(f'현재칸은 {i} {j} 주변 친구 {around} 빈칸 {blank}')
            # 친구가 많으면 갱신
            if max_around < around:
                max_around = around
                max_blank = blank
                mi = i
                mj = j
            # 주변 친구 수가 같은데 빈칸 수가 더 많다면 갱신
            elif max_around == around and max_blank < blank:
                max_blank = blank
                mi = i
                mj = j
    # 최종 넣기..
    if max_around == 0 and max_blank == 0:
        mi = last[0][0]
        mj = last[0][1]
    # print(f'최종 {mi}, {mj}')
    my_class[mi][mj] = me


N = int(input())
likes = [[0,0,0,0] for _ in range(N*N + 1)]
my_class = [[0]*N for _ in range(N)]
for k in range(N**2):
    students = list(map(int,input().split()))
    me = students[0]
    friends = students[1:]
    likes[me] = friends

    if k == 0:
        my_class[1][1] = me
        continue


    insert_student(me, friends)
    # print(f'{k}번째 학생 앉음')
    # for i in range(N):
    #     print(my_class[i])
point = 0
# 만족도 조사
for i in range(N):
    for j in range(N):
        cnt = 0
        me = my_class[i][j]
        friends = likes[me]
        for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            ni = i + di
            nj = j + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            # 내 친구가 있다면 개수 추가
            if my_class[ni][nj] in friends:
                cnt += 1

        if cnt == 1:
            point += 1
        elif cnt == 2:
            point += 10
        elif cnt == 3:
            point += 100
        elif cnt == 4:
            point += 1000
print(point)





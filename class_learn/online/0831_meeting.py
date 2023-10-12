N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meet = []
for i in range(N):
    meet.append([a[i*2],a[i*2+1]])
# 뒤에꺼 기준으로 정렬
meet.sort(key=lambda x:x[1])
# 회의실 비어있는상황 포함
meet = [[0,0]]+meet

S = []
j = 0

for i in range(1,N+1):
    # 앞순서의 회의가 끝나는 시간 보다 늦게 시작하면 포함
    if meet[i][0] >= meet[j][1]: # si>=fj
        S.append(i)
        j = i




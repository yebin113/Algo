import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 신청서
    N = int(input())

    time = []
    # 화물차 이용시간
    for i in range(N):
        s,e = map(int,input().split())
        time.append([s,e])
    # 끝나는 시간에 정렬(빨리 끝나는 순)
    time.sort(key=lambda x:x[1])
    S =[]
    j = 0
    # 이용시간 배열을 돌면서
    for i in range(len(time)):
        # 현재의 이용시간이 끝나고 난 뒤에 시작하면 추가해준다
        if time[i][0] >= time[j][1]:
            S.append(i)
            # 그리고 이용 팀 갱신
            j = i
    # 회의 맨 처음도 추가해줘야함
    print(f'#{tc} {len(S)+1}')
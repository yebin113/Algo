import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())        # 정사각형 한변의 길이
    arr = [list(map(int, input().split())) for i in range(N)]   # 배열 받기
    # 0이면 빈공간, 1이면 N극 2면 S극

    cnt = 0
    for j in range(N):
        flag = []
        # N극부터 시작
        changed = 1
        for i in range(N):
            if arr[i][j] != 0:
                # 값이 0이 아니면 리스트에 담습니다
                flag.append(arr[i][j])

        # 각자  위 아래에 생기는 자석에 달라붙는 자석 제거
        while flag[0] != 1:
            flag.pop(0)

        while flag[-1] != 2:
            flag.pop()

        for f in range(len(flag)-1):  # 자석들을 순회
            if flag[f] == 1 and flag[f+1] == 2:     # 교착상태 세기
                cnt += 1

    print(f'#{tc} {cnt}')
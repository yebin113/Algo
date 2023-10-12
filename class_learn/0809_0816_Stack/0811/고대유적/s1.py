import sys
sys.stdin = open("input.txt")

T = int(input())


# 연속된 1의 길이 코드와 동일
# 런타임 에러
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 최종 최대길이
    max_length = 0
    # 행렬 같은 반복문으로 사용 -> i랑 j만 바꿔주면 됨
    for i in range(N):
        length1 = 0
        length2 = 0
        for j in range(M):
            # 행
            if arr[i][j] == 1:
                length1 += 1
            # 0이면 길이 초기화
            else:
                length1 = 0
            # 열
            if arr[j][i] == 1:
                length2 += 1
            else:
                length2 = 0
            # 최댓값 갱신
            if max_length < max(length1,length2):
                max_length = max(length1,length2)

    print(f'#{tc} {max_length}')
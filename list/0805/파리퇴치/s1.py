import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # M은 파리채 크기
    N, M = map(int, input().split())
    # 해당 영역에 존재하는 파리의 개수가 담긴 배열
    arr = [list(map(int, input().split())) for i in range(N)]
    # 죽인 파리 최댓값
    max_sum_fly = 0
    # 파리채만큼 뺀 범위 내를 순회 out of range 방지
    for i in range(0,N-M):
        for j in range(0, N - M):
            # 각 위치마다 파리의 마리수를 구해야함
            sum_fly = 0
            # 파리채만큼 순회
            for k in range(i,i+M):
                for l in range(j, j+M):
                    # 영역내의 파리를 모두 더함
                    sum_fly += arr[k][l]
            # 최댓값 갱신
            if max_sum_fly < sum_fly:
                max_sum_fly = sum_fly

    print(f'#{tc} {max_sum_fly}')
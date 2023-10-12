import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_hap = 99*N
    # 일단 첫번째 값은 다 돌아보기...
    for i in range(N):
        # 겹치는 세로줄 체크
        visited = [0]*N
        # 현재 세로줄 체크
        visited[i] = 1
        hap = arr[0][i]
        j = 1
        while j < N:
            # 중복값이 있을거같으니 인덱스와 함께 저장
            sort_arr = list(enumerate(arr[j]))
            # x[1]로 (값) 정렬
            sort_arr.sort(key=lambda x:x[1])
            for k in range(N):
                # 해당 자리수가 차지되지 않았으면 그걸로..
                if visited[sort_arr[k][0]] == 0 :
                    hap += sort_arr[k][1]
                    visited[sort_arr[k][0]] = 1
                    break
            j += 1
        # 최소 구하기...
        if min_hap > hap:
            min_hap = hap


    print(f'#{tc} {min_hap}')
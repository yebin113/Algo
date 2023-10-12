import sys
sys.stdin = open("input.txt")


def f(i, N):
    global min_hap
    if i == N:  # 순열완성
        # 출발( 회사 -> 첫번째 고객의 거리)
        ans = abs(start[0]-p[0][0])+abs(start[1]-p[0][1])
        # 고객들 집을 순회하며 이동거리를 더함
        for k in range(N-1):
            ans += abs(p[k+1][0]-p[k][0])+abs(p[k+1][1]-p[k][1])
            # 현재 값이 최소거리보다 커버린다면 가지치기
            if ans > min_hap:
                return
        # 맨마지막에 집으로 돌아가는 거리 더해주기
        ans += abs(end[0] - p[-1][0]) + abs(end[1] - p[-1][1])
        # 최소합 갱신
        if ans < min_hap:
            min_hap = ans

        return
    else:
        # 자릿수 사용여부로 순열 만들기
        for j in range(N):
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                f(i+1,N)
                used[j] = 0




T = int(input())

for tc in range(1, T+1):
    # 고객 수
    N = int(input())
    # 회사의 좌표, 집의 좌표, N명의 고객의 좌표
    xy = list(map(int, input().split()))
    # 회사의 좌표
    start = [xy.pop(0),xy.pop(0)]
    # 집의 좌표
    end = [xy.pop(0),xy.pop(0)]
    # 고객들만의 좌표
    arr = []
    for i in range(N):
        arr.append([xy[2*i],xy[2*i+1]])
    # 순열을 저장할 배열
    p = [[0,0]]*N
    # 사용 여부 판단할 배열
    # print(arr)
    min_hap = 100000000000000000000000000
    # 함수 호출(min_hap global로 변경)
    f(0,N)
    print(f'#{tc} {min_hap}')
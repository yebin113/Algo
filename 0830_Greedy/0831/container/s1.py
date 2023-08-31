import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 컨테이너 수 N과 트럭수 M
    N, M = map(int,input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    # 무거운 것부터
    container.sort()
    # 적재용량 높은것부터 정렬
    truck.sort()
    # 맨끝의 트럭부터
    j = M-1
    kg = 0
    # 무거운 것부터 트럭에 적재할 수 있는지
    for i in range(N-1,-1,-1):
        # 트럭을 다 썼다면 탈출
        if j == -1:
            break
        # 트럭의 적재용량이 컨테이너보다 크다면
        if truck[j] >= container[i]:
            # 옮길 수 있는 컨테이너 용량
            kg += container[i]
            # 트럭을 사용함
            j -= 1

    print(f'#{tc} {kg}')
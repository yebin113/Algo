# 누적 누적 해서 비교하는 코드도 짜보기!
import sys
sys.stdin = open("input.txt")
T = int(input())

for tc in range(1, T+1):
    # N 예약손님 수, M초의 시간마다 K개의 붕어빵 만듬
    N,M,K = map(int,input().split())
    # 예약손님 도착시간(정렬되어있지 않다)
    arr = list(map(int, input().split()))
    arr.sort()
    result = 'Possible'
    for i in range(N):
        if i +1 > arr[i] //M*K:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')
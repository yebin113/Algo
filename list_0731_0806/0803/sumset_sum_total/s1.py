import sys
sys.stdin = open("input.txt")



T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)  # n : 원소의 개수
    ans = 0
    for i in range(1, 1 << n):  # 1부터 시작하는 이유 -> 공집합 제거, l<<n : 부분 집합의 개수
        sum_set = 0     # 각 부분집합의 반복을 돌때 0으로 초기화
        for j in range(n):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번 비트가 1인경우
                sum_set += arr[j]   # 부분집합의 합
        if sum_set == 0:        # 부분집합의 합이 0이라면
            ans = 1             # 존재함
            break


    print(f'#{tc} {ans}')





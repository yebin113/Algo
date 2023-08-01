"""
N개의 양의 정수가 첫번째부터 N번째까지 주어진다. 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 하시오.
단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.
예를 들어, {1, 1, 2, 3, 3} 가 주어지면 최대값의 위치는 5이고, 최소값의 위치는 1이다. 따라서 두 값 차이의 절대값은 4이다.
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0

    for i in range(1, N):
        # 같은것도 포함하면 같은 값이 있을때 더 후자의 인덱스가 추출
        if arr[min_idx] > arr[i]:
            min_idx = i
        # 최댓값은 더 마지막이 나오게 같을 경우도 인덱스 재할당
        if arr[max_idx] <= arr[i]:
            max_idx = i

    # 절댓값 함수 대신 사용
    if max_idx > min_idx:
        ans = max_idx - min_idx

    else:
        ans = min_idx - max_idx

    print(f'#{tc} {ans}')

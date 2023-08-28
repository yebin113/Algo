T = int(input())

for tc in range(1, T+1):
    # 당근의 개수
    N = int(input())
    # 당근의 크기
    arr = list(map(int, input().split()))
    # 범위 나누기
    # 0 ~ i / i+1 ~ j / j+1 ~ N-1
    # i -> 0~N-3
    # j -> i+1 ~ N-2


    arr.sort()  # 당근을 크기순으로 정렬
    min_v = 10000       # 포장별 최소 개수 차이
    for i in range(N-2):
        for j in range(i+1,N-1):
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:   # 같은 크기의 당근을 가이로 박스를 나눠서는 안됨
                small = i + 1   # 소 상자에 들어간 당근 개수
                mid = j -1      # 중 상자에 들어간 당근 개수
                large = N-1 -j  # 대 상자에 들어간 당근 개수
                if small <= N//2 and mid <= N//2 and large <= N//2:
                    if min_v > max(small,mid,large) - min(small,mid,large):
                        min_v = max(small, mid, large) - min(small, mid, large)
    if min_v == 10000:
        min_v = -1
    print(f'#{tc} {min_v}')


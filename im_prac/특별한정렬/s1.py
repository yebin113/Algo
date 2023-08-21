import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_list = []

    for i in range(N-1):
        max_num = 0
        max_idx = 0
        min_num = 100
        min_idx = 0
        for j in range(i,N):
            if max_num < arr[j]:
                max_num = arr[j]
                max_idx = j
            if min_num > arr[j]:
                min_num = arr[j]
                min_idx = j
        arr[i],arr[max_idx] = arr[max_idx],arr[i]
        arr[i+1],arr[min_idx] = arr[min_idx],arr[i+1]

    print(f'#{tc}',*arr)
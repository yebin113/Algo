import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count_light = 0
    for i in range(2,N-2):
        around = [arr[i-2],arr[i-1],arr[i+1],arr[i+2]]
        max_around = 0
        # 주변 건물 높이중 최댓값 구하기
        for j in range(4):
            if max_around < around[j]:
                max_around = around[j]
        # 현재 높이가 더 높으면 그 차를 더한다
        if arr[i] > max_around:
            count_light += arr[i] - max_around


    print(f'#{tc} {count_light}')
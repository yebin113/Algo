import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dump = 0
    # 덤프 반복
    while 1:
        dump += 1
        max_box = 0
        max_idx = 0
        min_box = 1000
        min_idx = 0
        # 최댓값과 최솟값 그리고 그 인덱스를 구합니다
        for i in range(100):
            if max_box <= arr[i]:
                max_box = arr[i]
                max_idx = i
            if min_box >= arr[i]:
                min_box = arr[i]
                min_idx = i
        # 덤프횟수가 N번이 되면 최대 - 최소 다시 구하고 출력하고 탈출
        if dump == N+1:
            print(f'#{tc} {max_box - min_box}')
            break
        arr[max_idx] -= 1
        arr[min_idx] += 1





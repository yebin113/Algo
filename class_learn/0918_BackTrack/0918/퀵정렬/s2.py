import sys

sys.stdin = open("input.txt")


# 중간값을 찾는 과정
def partition(arr, l, r):
    pivot = arr[r]
    # i = 작은 요소들을 추적
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 피벗 위치 교환
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    # 피벗의 새 위치를 반환
    return i + 1


def quick(arr, l, r):
    # 왼쪽이 오른쪽보다 클때
    if l < r:
        pivot = partition(arr, l, r)
        # 범위 나눠서 재귀
        quick(arr, l, pivot-1)
        quick(arr, pivot + 1, r)




T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(arr, 0, N - 1)
    print(f'#{tc} {arr[N // 2]}')

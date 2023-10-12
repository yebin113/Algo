import sys

sys.stdin = open("input.txt")

T = int(input())


def merge(left, right):

    result = []

    # 한 쪽이 빌 때까지 반복
    while len(left) > 0 or len(right) > 0:
        # 둘 다 남아 있으면, 두 리스트의 가장 앞에 있는 것 중 작은 것을 선택하여 result 에 추가
        if len(left) > 0 and len(right) > 0:

            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # 한 쪽만 남아있으면, 남은것을 모두 result 에 추가
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            cnt = 1
            result.append(right.pop(0))
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) //2
    left = arr[:middle]
    right = arr[middle:len(arr)]
    left = merge_sort(left)
    right = merge_sort(right)
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)

    print(f'#{tc} {arr[N // 2]} {cnt}')

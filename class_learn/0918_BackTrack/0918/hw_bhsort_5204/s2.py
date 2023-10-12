import sys

sys.stdin = open("input.txt")

T = int(input())

def merge(left, right):

    result = []
    i = 0
    j = 0
    # 한 쪽이 빌 때까지 반복
    while i < len(left) or j < len(right):
        # 둘 다 남아 있으면, 두 리스트의 가장 앞에 있는 것 중 작은 것을 선택하여 result 에 추가
        if i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # 한 쪽만 남아있으면, 남은것을 모두 result 에 추가
        elif i<len(left):
            result.append(left[i])
            i += 1
        elif j<len(right):
            result.append(right[j])
            j += 1

    return result

def merge_sort(unordered_list):
    global cnt
    # 길이가 1인 배열까지 나누면 stop
    if len(unordered_list) == 1:
        return unordered_list

    left = []
    right = []
    middle = len(unordered_list) // 2
    # 왼쪽을 따로 리스트에 저장
    for el in unordered_list[:middle]:
        left.append(el)

    # 오른쪽을 따로 리스트에 저장
    for el in unordered_list[middle:]:
        right.append(el)

    left = merge_sort(left)
    right = merge_sort(right)
    # 문제에서 요구하는 사항
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)

    print(f'#{tc} {arr[N // 2]} {cnt}')

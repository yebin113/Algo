# 5204. 병합 정렬

# merge 함수
def merge(left, right):
    rst = []
    global cnt

    # rst2를 세는 부분
    if left[-1] > right[-1]:
        cnt += 1

    # 둘 다 빌 때까지 left와 right를 비교해서 작은 값을 먼저 rst에 넣기
    while len(left) > 0 or len(right) > 0:

        # 1. 둘 다 남아 있을 때
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                rst.append(left.pop(0))
            else:
                rst.append(right.pop(0))

        # 2. 한쪽만 남아 있을 때
        elif len(left) > 0:
            rst.append(left.pop(0))
        elif len(right) > 0:
            rst.append(right.pop(0))

    return rst

# 병합 정렬 함수
def merge_sort(arr):
    # [종료조건]
    # 1. 나눌 배열의 길이가 1이면 종료
    if len(arr) == 1:
        return arr

    # [수행내용]
    # 1. arr를 받아서 왼쪽, 오른쪽으로 나누기
    left = []
    right = []
    middle = len(arr) // 2  # 왼쪽, 오른쪽 나누기 위한 중앙값

    # 2. 왼쪽 배열을 저장
    for element in arr[:middle]:
        left.append(element)
    # 3. 오른쪽 배열을 저장
    for element in arr[middle:]:
        right.append(element)

    # 4. 왼쪽/오른쪽 배열을 각각 다시 나누기(재귀)
    left = merge_sort(left)
    right = merge_sort(right)

    # 5. 나눈 값을 정렬해서 합치기 -> merge 함수
    return merge(left, right)


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())  #N: 정수의 개수
    L = list(map(int, input().split()))  #L: N개의 정수를 가진 리스트
    cnt = 0  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 셀 변수

    sorted_arr = merge_sort(L)
    rst1 = sorted_arr[N//2]  # N//2번째 원소
    rst2 = cnt #오른쪽 원소가 먼저 복사되는 경우의 수
    print(f'#{tc} {rst1} {rst2}')
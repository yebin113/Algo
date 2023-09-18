# 이진 검색 - 재귀
arr = [2, 4, 7, 9, 11, 19, 23]
# 데이터 정렬
arr.sort()


# 함수 한번 호출 때마다 low, high 변수가 바뀌어서 사용됨
def binarySearch(low, high, target):
    # 기저조건 : 언제까지 재귀호출을 반복할 것인가?
    # 데이터를 못찾음
    if low > high:
        return -1
    mid = (low + high) // 2
    # 가운데 값이 정답인 경우
    if arr[mid] == target:
        return mid
    # 정답보다 작은 경우
    elif arr[mid] < target:
        binarySearch(mid + 1, high, target)
    # 정답보다 큰 경우
    else:
        binarySearch(low, mid - 1, target)

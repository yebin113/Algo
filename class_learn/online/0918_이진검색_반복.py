# 이진 검색 - 반복문
arr = [2,4,7,9,11,19,23]
# 데이터 정렬
arr.sort()


def binarySearch(target):
    low = 0
    high = len(arr)-1

    #  low >= high 라면 데이터를 못찾은 경우
    while low <= high:
        mid = (low + high) // 2
        # 데이터를 찾은경우(가운데 값이 정답)
        if arr[mid] == target:
            return mid
        # 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid + 1
        # 정답보다 큰 경우
        else:
            high = mid - 1
    return '해당 데이터는 없습니다.'


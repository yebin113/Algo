import sys
sys.stdin = open("input.txt")

T = int(input())

# 타겟이랑 배열이 주어진다
def binsearch(target,arr):
    # 시작 인덱스
    low = 0
    # 끝 인덱스
    high = len(arr)-1
    # 중간 인덱스

    # 구간 탐색 기록
    search = ''
    # 구간이 존재할때
    while low <= high:
        mid = (high + low) // 2
        # 중간 값이 타겟이라면
        if arr[mid] == target:
            # 구간탐색 기록을 리턴합니다
            return search
        # 중간값보다 타겟이 작을때
        elif arr[mid] > target:
            # 끝 인덱스를 중간 -1 로 땡기기
            high = mid - 1
            # 구간 탐색에 왼쪽 기록
            search += 'l'
        # 중간값보다 타겟이 클때
        else:
            # 시작인덱스를 중간 +1 로 땡긴다
            low = mid + 1
            # 구간 탐색에 r을 추가
            search += 'r'
    # 값이 없다면 -1 리턴
    return -1


for tc in range(1, T+1):
    N, M = map(int,input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    # 정렬
    arrA= sorted(arrA)
    # 조건에 맞는 수가 있는지 셀 값
    cnt = 0
    # B에 들어있는 수들을 순차적으로 검사
    for B in arrB:
        result = binsearch(B,arrA)
        # 값이 없거나, 연속된 방향으로 검색했을때는 넘기기
        if result == -1 or 'll' in result or 'rr' in result:
            continue
        # continue에 안걸린 경우 카운트
        cnt += 1

    print(f'#{tc} {cnt}')
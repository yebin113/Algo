import sys

sys.stdin = open("input.txt")


def count_bin(P, A):
    counts = 0

    l = 1       # 왼쪽 구간
    r = P       # 오른쪽 구간
    while l <= r:    # 구간이 존재하는 경우( 왼쪽 구간의 시작이 오른쪽 구간보다 작거나 같을때)
        middle = (l+r) // 2  # 중간값
        counts += 1  # 횟수 세기

        if A > middle:  # 중간 값보다 A가 크면
            l = middle  # 왼쪽의 값을 중간값으로 변경

        elif A < middle:    # 중간값이 A보다 크면
            r = middle      # 오른쪽의 값을 중간값으로 변경

        else:
            break   # 중간값이 A 라면 탈출

    return counts   # 센 횟수 리턴


T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())  # 전체 페이지 쪽수, A가 찾을 쪽수 , B가 찾을 쪽수

    if count_bin(P, A) < count_bin(P, B):   # 센 횟수가 적은쪽을 출력
        ans = 'A'
    elif count_bin(P, A) == count_bin(P, B):    # 비기면 0
        ans = 0
    else:
        ans = 'B'

    print(f'#{tc} {ans}')

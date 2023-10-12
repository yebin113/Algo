import sys

sys.stdin = open("input.txt")

T = int(input())


def find(level, total):
    global ans
    # 가지 치기
    if total >= ans:
        return
        # 기저조건

    # 12달 이상일때 TOTAL과 최소를 비교 후 갱신
    if level >= 12:
        if ans > total:
            ans = total
        return

    find(level + 1, total + arr[level] * day1)
    find(level + 1, total + month1)
    find(level + 3, total + month3)
    return


for tc in range(1, T + 1):
    day1, month1, month3, year = map(int, input().split())
    # 운영 계획
    arr = list(map(int, input().split()))
    # 최소 비용(년으로 시작)
    ans = year
    find(0, 0)

    print(f'#{tc} {ans}')

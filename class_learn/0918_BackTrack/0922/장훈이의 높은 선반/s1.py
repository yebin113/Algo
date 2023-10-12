import sys

sys.stdin = open("input.txt")
"""
탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데 탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑
"""


def recur(level, acc_height):
    # level : 점원 어디까지? 체크용
    # acc_height : 더해 갈 숫자
    global ans
    # 최솟값 관리
    # 만약 선반높이를 넘었다면
    if acc_height >= B:
        # 정답과 높이를 비교해보고 리턴(가지치기)
        ans = min(ans, acc_height)
        return
    # 기저조건 : N명 다 뽑았으면 리턴
    if level == N:
        return
    # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + arr[level])
    # 해당 점원을 탑에 안 쓸 경우
    recur(level + 1, acc_height)


T = int(input())

for tc in range(1, T + 1):
    # 점원의 수와 원하는 높이
    N, B = map(int, input().split())
    # 점원 키 리스트
    arr = list(map(int, input().split()))
    # 최소를 구해야 해서 가장 큰 수로 저장
    ans = int(1e9)
    recur(0, 0)
    print(f'#{tc} {ans - B}')

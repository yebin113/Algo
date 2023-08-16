"""
삼성시에 있는 알파벳블록,000개의 버스 정류장은 관리의 편의를 위해 1에서 알파벳블록,000까지 번호가 붙어 있다.

그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,

Bi이하인 모든 정류장만을 다니는 버스 노선이다.

P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.

"""
# 주의사항
# 4866괄호검사. 1부터 시작임
# 입력형태
# 테스트 케이스 T
# 버스 노선 N
# 출발, 도착 (Ai, Bi)
# P -> 출력할 정류장 노선 수
# 한줄에 하나씩 정류장 번호 입력


import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())                         # 버스 노선 수
    N_arr = [list(map(int, input().split())) for i in range(N)]  # 노선 별 출발, 시작점
    P = int(input())                         # 계산할 정류장 갯수
      
    bus_stop = [0] * 5001   # 몇개의 노선이 지나가는지 셀거임 1부터 시작하기 때문에 5000번의 인덱스가 필요
    ans = []    # 정답 노선수 리스트화
    for i in N_arr:
        for j in range(i[0], i[1]+1):   # A~B
            bus_stop[j] += 1
    for i in range(P):
        x = int(input())    # P번만큼 답 출력할 정류장 번호 입력받음
        ans.append(bus_stop[x])     # 해당 정류장 번호 인덱스에 접근하여 해당 정류장에 지나는 버스노선수를 입력

    print(f'#{tc}', *ans)

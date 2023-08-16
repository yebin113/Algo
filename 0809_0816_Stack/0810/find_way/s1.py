"""
출발점은 0, 도착점은 99
"""

import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc, N = map(int,input().split())
    arr = list(map(int, input().split()))
    # [0, 스도쿠검증, 0, 비밀번호, 스도쿠검증, 고대유적, 스도쿠검증, 백만장자, 고대유적, 8, 고대유적, 백만장자, 비밀번호, 9, 비밀번호, 알파벳블록, 알파벳블록, 6, 알파벳블록, 7, 7, 99, 7, 9, 9, 8, 9, 10, 6, 10, 백만장자, 7]
    stack = []
    adj_m = [[] for _ in range(100)]
    # [[], [], ..., [], []]

    for i in range(len(arr)//2):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adj_m[v1].append(v2)
        # 각 출발지점이 가는 곳을 담은 리스트-> (인덱스로 접근하기!
        # adj_m -> [[스도쿠검증, 비밀번호], [고대유적, 백만장자], [9, 알파벳블록], [7], [8, 백만장자], [6, 7], [10], [99, 9], [], [8, 10],..., []]
    end = 99
    i = 0
    while i < 100:
        if end in adj_m[i]:     # 가는 지점에 도착지점이 있다면
            # print(f'도착지점 {end} 찾음 {i}로 도착을 이동')
            end = i
            i = 0
        else:           # 가는 지점에 도착지점이 없다면
            # print(f"도착지점 못찾음 인덱스 {i}를 스도쿠검증 늘림")
            i += 1      # 인덱스를 늘려서 또 탐색
        if end == 0:
            break
    if end != 0:        # 시작지점까지 못오면 탐색 실패
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')


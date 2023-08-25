"""
숙소는 긴 복도를 따라 400개의 방이 마주보고 배열되어있음
1 3 5 7 9 .... 399
2 4 6 8 10 ... 400
모든학생들은 현재위치에서 자신의 방으로 돌아가려고하는데 만약 두학생이 이동코스가 겹치면 안됨
제일 적은 시간으로 이동할 수 있는걸 구해야함

버스노선과 같이 모든 이동동선을 세보고 겹치는 구간마다 단위시간 +1
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 학생의 수
    N = int(input())
    # 복도
    arr = [0]*201
    # N줄에 걸쳐 현재 방번호 -> 도착 방번호가 주어짐 ★★★ 도착번호가 더 작을 수도 있다.
    for n in range(N):
        start, end = map(int,input().split())
        # 방번호 -> 짝수//2  (홀수 +1) //2
        # 한줄로 처리하는 법 -> (방번호 +방번호 %2)//2
        start = (start + start % 2)//2
        end = (end + end % 2)//2

        for i in range(min(start,end),max(start,end) +1):
            arr[i] += 1

    # 최댓값이 단위시간의 최대시간
    print(f'#{tc} {max(arr)}')
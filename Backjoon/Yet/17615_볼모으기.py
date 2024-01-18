import sys
input = sys.stdin.readline

N = int(input())
balls = list(input().rstrip())

# 한가지인 경우
cntR = balls.count('R')
cntB = N - cntR
result = min(cntR,cntB)
if cntB*cntR == 0:
    print(0)

else:
    start = balls[0]
    end = balls[-1]
    cnt_left = 0
    cnt_right = 0
    check_l = False
    check_r = False
    for i in range(N):
        if balls[i] != start:
            break
        cnt_left +=1
    for i in range(N-1,-1,-1):
        if balls[i] != end:
            break
        cnt_right +=1

    if start == 'R':
        result = min(result,cntR - cnt_left)
    else:
        result = min(result, cntB - cnt_left)

    if end == 'R':
        result = min(result,cntR - cnt_right)
    else:
        result = min(result, cntB - cnt_right)
    print(result)


import sys
input = sys.stdin.readline

N = int(input())
balls = list(input())
# 한가지인 경우
cntR = balls.count('R')
cntB = N - cntR
if cntB*cntR == 0:
    print(0)

else:
    # 위치 저장
    locate = {
        'R':[],
        'B':[]
    }
    for i in range(N):
        locate[balls[i]].append(i)

    # 각 공을 오른쪽, 왼쪽으로 밀때의 변경 횟수에 대해 비교하고 적은 수를 출력
    Rr = 0
    Rb = 0
    Lr = 0
    Lb = 0
    for i in range(max(cntR,cntB)):
        try:
            if locate['R'][i] != N - cntR + i:
                Rr += 1
            if locate['R'][i] != i:
                Lr += 1
        except:
            continue
        try:
            if locate['B'][i] != N - cntB + i:
                Rb += 1
            if locate['B'][i] != i:
                Lb += 1
        except:
            continue

    print(min(Rr,Lr,Rb,Lb))


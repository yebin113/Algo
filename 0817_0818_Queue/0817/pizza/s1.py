
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 화덕의 크기 N과 피자 개수 M
    N, M = map(int,input().split())
    #  M개의 피자에 뿌려진 치즈의 양을 나타내는 배열
    cheese = list(map(int, input().split()))
    cheese_list = []

    # 인덱스를 확인하기 위해 같이 넣음
    for i in range(M):
        cheese_list.append([i, cheese[i]])
    Q = [0] * N

    # 피자 먼저 N개 넣음
    for i in range(N):
        Q[i] = cheese_list.pop(0)

    # 남은 피자가 1개일때까지
    while len(Q) > 1:
        Q_copy = Q[:]
        # 가장 먼저 들어간 피자의 치즈가 다 안 녹았다면
        if Q_copy[0][1] // 2 != 0:
            # print('다 안녹음',Q_copy[0])

            # 뒤로 밀기
            Q = Q_copy[1:]
            Q.append([Q_copy[0][0],Q_copy[0][1] // 2])
            # print('안쪽으로 들어감',[Q_copy[0][0],Q_copy[0][1] // 계산기])

        # 만약 치즈가 다 녹았다면

        else:
            # 첫번째 피자 나옴
            Q.pop(0)
            # print('녹음',Q.pop(0))

            # 남은 피자가 있다면 새로 넣기
            if len(cheese_list):
                Q.append(cheese_list.pop(0))
                # print('새로 넣음',Q[-1])


    print(f'#{tc} {Q[0][0]+1}')
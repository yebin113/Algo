from sys import stdin
import pprint
import copy
def how_many_kill(p1, p2, p3):
    board = copy.deepcopy(arr)
    # print('궁수들의 위치',p1,p2,p3)
    kill = 0
    forward = N - 1
    while forward >= 0:
        c1, c2, c3 = 1, 1, 1
        # print(f'적들이 얼마나 남았는지, 지금은 {N-1- forward}번째 턴')
        # pprint.pprint(board)
        for i in range(forward,-1,-1):
            for j in range(M):
                if board[i][j] == 1:
                    if c1 and can_kill((forward+1,p1), (i, j)):
                        c1 -= 1
                        kill += 1
                        board[i][j] = 0
                    elif c2 and can_kill((forward+1,p2), (i, j)):
                        c2 -= 1
                        kill += 1
                        board[i][j] = 0
                    elif c3 and can_kill((forward+1,p3), (i, j)):
                        c3 -= 1
                        kill += 1
                        board[i][j] = 0
                if c1 + c2 + c3 == 0:
                    break
            if c1 + c2 + c3 == 0:
                break
        forward -= 1
    return kill


# 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|
def can_kill(mine, enemy):
    mi, mj = mine
    ei, ej = enemy
    if abs(mi - ei) + abs(mj - ej) <= D:
        return True
    else:
        return False


# 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D
N, M, D = map(int, stdin.readline().split())
arr = []
for _ in range(N):
    # 0은 빈 칸, 1은 적이 있는 칸
    i = list(map(int, stdin.readline().split()))
    arr.append(i)
# 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다.
# 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고,
# 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격
# 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외

# 공격으로 제거할 수 있는 적의 최대 수를 출력

# 1. M칸중 세칸을 고르기
from itertools import combinations

zohap = list(combinations(range(M), 3))
many_kill = 0
for p1,p2,p3 in zohap:
    kill = how_many_kill(p1,p2,p3)
    many_kill = max(many_kill,kill)
print(many_kill)
# 2. 골라진 세 칸에서 제거할 수 있는 최대 적을 갱신
#     2.1 arr 맨 밑에서부터 올라감 (while)
#     2.2 궁수1, 궁수 2, 궁수 3이 조건에 맞는 적을 각 한명씩 퇴치할때까지 도는 (for)
#           다 퇴치하묜 break (다음턴)
# 적 퇴치하면 0으로 바꿔주기
#         arr이 맨 위까지 탐색하면 끝~

# import sys
# from itertools import permutations
# N = int(sys.stdin.readline())
# game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# # 조건
# # 1. 한 이닝에 3아웃이 발생하면 이닝 종료
# # 2. 9번 타자까지 공을 쳤는데 3아웃이 발생하지 않으면 이닝 종료하지않음
# # 3. 1번 이닝에서 6번 타자가 마지막이면 2번 이닝은 7번 타자부터 시작
# # 4. 경기가 시작하기 전에 타순을 정해줘야함, 단 4번타자는 고정 1번 선수
# order = [i for i in range(1,9)] # 고정된 4번타자 제외하고 순서를 정해주자.
# result = 0
# for x in permutations(order,8): # 8명의 순서의 조합을 따져본다.
#     x = list(x)
#     batter = x[:3] + [0] + x[3:] # 4번 조건. 1~3번 타자(랜덤 3명) / 1번 선수 (1번 선수) / 4~8번 타자(랜덤 5명)
#     number, point = 0, 0 # 타수와 점수
#     for i in range(N): # 각 이닝에 대해
#         out = 0 #이닝이 돌면 out은 0으로 초기화
#         p1 = p2 = p3 = 0 # 1~3루의 현재 상태
#         while out < 3: # 1번, 2번 조건. out이 3번이 되기 전까지 반복
#             #여기서부터 야구 룰
#             if game[i][batter[number]] == 0:
#                 out += 1
#             elif game[i][batter[number]] == 1:
#                 point += p3
#                 p1, p2, p3 = 1, p1, p2
#             elif game[i][batter[number]] == 2:
#                 point += p2 + p3
#                 p1, p2, p3 = 0, 1, p1
#             elif game[i][batter[number]] == 3:
#                 point += p1 + p2 + p3
#                 p1, p2, p3 = 0, 0, 1
#             elif game[i][batter[number]] == 4:
#                 point += p1 + p2 + p3 + 1
#                 p1, p2, p3 = 0, 0, 0
#             number += 1 # 타순 증가
#             if number == 9: #타순이 9가 되면
#                 number = 0 #다시 0으로 초기화
#     # 3번 조건. 이닝이 끝나도 number을 초기화 하지 않으므로 다음이닝에 타순 유지
#     result = max(result, point)
# print(result)



from itertools import permutations
import sys
input = sys.stdin.readline

def set_point(sequence):
    res = 0
    seq = 0
    for result in results:
        cnt_out = 0
        base1 = 0
        base2 = 0
        base3 = 0
        while cnt_out < 3:

            if result[sequence[seq]] == 0:
                # 아웃
                cnt_out += 1
            elif result[sequence[seq]] == 1:
                # 1루타
                res += base3
                base3 = base2
                base2 = base1
                base1 = 1

            elif result[sequence[seq]] == 2:
                # 2루타
                res += base2 + base3
                base3 = base1
                base1 = 0
                base2 = 1

            elif result[sequence[seq]] == 3:
                # 3루타
                res += base1 + base2 + base3
                base1 = 0
                base2 = 0
                base3 = 1

            else:
                # 4루타
                res += base1 + base2 + base3 + 1
                base1 = 0
                base2 = 0
                base3 = 0

            seq += 1
            if seq == 9:
                seq = 0
    return res


N = int(input())
results = []
for _ in range(N):
    r = list(map(int,input().split()))
    results.append(r)

order = [1,2,3,4,5,6,7,8]
max_point = 0
for hitters in permutations(order,8):

    hit = list(hitters[:3])
    hit.append(0)
    hit.extend(list(hitters[3:]))

    point = set_point(hit)
    max_point = max(max_point,point)


print(max_point)


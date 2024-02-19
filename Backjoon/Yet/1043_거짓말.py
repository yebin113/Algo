from itertools import product

N, M = map(int, input().split())
truth, *know_truth = map(int, input().split())
for i in range(truth):
    know_truth[i] -= 1
cnt = 0
party = [[0] * N for _ in range(M)]

# 파티에 오는 사람 기록
for i in range(M):
    come, *come_num = map(int, input().split())
    for j in range(come):
        person = come_num[j] - 1
        party[i][person] = 1
visit = []
for t_or_f in product(['T', 'F'], repeat=M):
    for i in range(M):


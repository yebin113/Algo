from itertools import combinations_with_replacement
N,M = map(int,input().split())
truth, *know_truth = map(int,input().split())
for i in range(truth):
    know_truth[i] -= 1
cnt = 0
party = [[0]*N for _ in range(M)]

# 파티에 오는 사람 기록
for i in range(M):
    come, *come_num = map(int,input().split())
    for j in range(come):
        person = come_num[j] - 1
        if person in know_truth:
            party[i][person] = 1
        else:
            party[i][person] = 2

for t_or_f in combinations_with_replacement(['T','F'],M):
    print(t_or_f)
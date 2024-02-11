from itertools import combinations

def is_Pick(listA):
    cnt = 0
    for p in pick:
        if p in listA:
            cnt += 1
    if cnt >= K:
        return True
    else:
        return False


N,M,K = map(int,input().split())
numbers = [i for i in range(1,N+1)]
pick = [i for i in range(1,M+1)]
cnt_all = 0
cnt_pick = 0
for number_set in combinations(numbers,M):
    cnt_all += 1
    if is_Pick(number_set):
        cnt_pick += 1
print(cnt_pick/cnt_all)


from itertools import combinations
N, M = map(int, input().split())
no_mix = [[] for _ in range(N)]
ice_cream = [i+1 for i in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    no_mix[a-1].append(b-1)
    no_mix[b-1].append(a-1)

cnt = 0
# print(no_mix)

for set_icecream in combinations(ice_cream,3):
    check = False
    # print(set_icecream)
    for i in range(3):
        # print(i, no_mix[set_icecream[i]-1])
        for j in range(3):
            if i == j:
                continue
            if set_icecream[j]-1 in no_mix[set_icecream[i]-1]:
                check = True
                break
        if check:
            break
    if check == False:
        cnt += 1

print(cnt)

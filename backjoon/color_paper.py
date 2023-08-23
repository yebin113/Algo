# 색종이 장수
N = int(input())

paper_total = []
for i in range(N):
    paper_set = set()
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            paper_set.add((i,j))
    paper_total.append(paper_set)

for i in range(N):
    now_set = paper_total[i]
    for j in range(N):
        if i == j :
            continue
        now_set = now_set - paper_total[j]
        print(now_set)
    print(len(now_set))


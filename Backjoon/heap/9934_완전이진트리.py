"""
루트노드의 인덱스를 찾고, 층수 tree에 넣어준다
가장 상위 루트는 step K임
step은 -1
start 부터 루트인덱스 -1 까지,
루트인덱스 + 1부터 end로 범위를 줄여나가며 재귀를 돌려준다

"""

def find_root(step,start,end):
    if step == 0:
        return
    root_idx = start+ 2 ** (step - 1) - 1
    tree[step].append(building[root_idx])
    find_root(step-1, start, root_idx-1)
    find_root(step - 1, root_idx +1, end)


K = int(input())
building = list(map(int,input().split()))
tree = [[] for _ in range(K+1)]
find_root(K,0,len(building))
for i in range(K,0,-1):
    print(*tree[i])
# 0 ~ 9
# make set - 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모

# find-set
def find_set(x):
    if parent[x] == x:
        return x
    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

# union
def union(x, y):
    check = False
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        check = True
        # print('사이클발생')
        return check

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x

    else:
        parent[x] = y

    return check

from sys import stdin
cnt = 0
while True:
    cnt += 1
    n,m = map(int,stdin.readline().split())
    if n == 0 and m==0:
        break
    parent = [i for i in range(n+1)]
    check  = 0
    for _ in range(m):
        f,t = map(int,stdin.readline().split())
        if union(f,t):
            check +=1


    # print(parent)
    tree = len(set(parent))-1 - check
    print(f'Case {cnt}:',end=' ')
    if tree<=0:
        print('No trees.')
    elif tree > 1:
        print(f'A forest of {tree} trees.')
    elif tree==1:
        print('There is one tree.')


import sys
sys.stdin = open("input.txt")

T = int(input())
# find-set
def find_set(x):
    if couple[x] == x:
        return x

    # 경로 압축
    couple[x] = find_set(couple[x])
    return couple[x]


def union(x,y):
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:

        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        couple[y] = x
    else:
        couple[x] = y

for tc in range(1, T+1):
    N,M = map(int,input().split())
    couple = [i for i in range(N)]
    arr = list(map(int, input().split()))

    for i in range(M):
        p1 = arr[2*i]-1
        p2 = arr[2*i+1]-1
        # 병합
        union(p1,p2)
    for i in range(N):
        find_set(i)
    # 중복삭제
    set_couple = list(set(couple))

    print(f'#{tc} {len(set_couple)}')
import sys

input = sys.stdin.readline


def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b, know_truth):
    a = find(parent, a)
    b = find(parent, b)
    # 파티에 같이 참석하는 사람들중에 진실을 알고있는 사람 존재한다면
    # 부모노드를 그사람으로 함
    if a in know_truth and b in know_truth:
        return

    if a in know_truth:
        parent[b] = a

    elif b in know_truth:
        parent[a] = b

    else:
        if a < b:
            parent[b] = a

        else:
            parent[a] = b


n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]

# 파티 정보기록
parties = []
# union find 사용할 부모노드
parent = list(range(n + 1))

for _ in range(m):
    # 오는 사람 기록
    people_num, *people_come = map(int, input().split())

    for i in range(people_num - 1):

        union(parent, people_come[i], people_come[i + 1], know_truth)

    parties.append(people_come)

ans = 0
for party in parties:
    for i in range(len(party)):
        # 파티중에 진실을 알고 있는 사람이 있다면, 거짓말을 못한다
        if find(parent, party[i]) in know_truth:
            break

    else:
        ans += 1

print(ans)
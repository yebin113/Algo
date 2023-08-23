data = [input().split() for i in range(100)]


# 자식노드가 없을 때, 인덱스를 맞추자
data.insert(0,[0,0,0,0])

for d in data:
    while len(d) != 4:
        d.append('0')

# 데이터 인풋 -> 우리가 가공해서 처리해야 할 데이터를 받는다
# 우리가 활용하기 편한 자료구조를 택하고 전처리를 한다

# IM:
# 주어진 데이터를 "적절한 자료구조"에 담아
# 핵심 : 2차원 배열


# 힙 -> 트리의 한 종류
# 최댓값 최솟값 -> 우선순위 큐

# 트리에서 삽입과 삭제가 이루어진다
# 루트노드가 가장 높은 우선순위를 갖는다
# node 삭제를 할때, 반드시 루트 노드를 삭제한다
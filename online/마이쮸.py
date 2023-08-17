from collections import deque
# deque는 속도가 빠름
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q.popleft())
print(q.popleft())
print(q.popleft())

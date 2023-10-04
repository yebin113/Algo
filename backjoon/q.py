def push(item):
    q.append(item)

def front():
    if len(q):
        print(q[0])
    else:
        print(-1)
def back():
    if len(q):
        print(q[-1])
    else:
        print(-1)

def pop():
    if len(q):
        print(q.popleft())
    else:
        print(-1)

def size():
    print(len(q))

def empty():
    if len(q):
        print(0)
    else:
        print(1)


from collections import deque
N = int(input())
q = deque()
for i in range(N):
    arr = list(input().split())
    if arr[0]=='push':
        push(int(arr[1]))
    elif arr[0] =='pop':
        pop()
    elif arr[0] =='front':
        front()
    elif arr[0] =='back':
        back()
    elif arr[0] =='empty':
        empty()
    elif arr[0] =='size':
        size()


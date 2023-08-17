def enQ(data):
    global rear
    if rear == Q_size -1:   # 가득 차면
        print('Q is Full')
    else:
        rear += 1
        Q[rear] = data


def deQ():
    global front
    if front == rear:       # 비어있으면
        print('큐가 비어이씀')
        return
    else:
        front += 1
        return Q[front]


Q_size = 3
Q = [0] * 3
rear = -1
front = -1
enQ(1)
enQ(2)
enQ(3)


while front != rear:
    front += 1
    print(Q[front])
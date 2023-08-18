def enq(data):
    global rear
    global front

    # deq를 수행하지 않으면 꽉차기는 매한가지
    # 꽉차지 않으려면 덮어쓰면 되는데 이러면 deq 수행할때 나중에 들어온게 나올수도
    if (rear + 1) % cQsize == (front+1):
        #  꽉찼을때 가장 먼저 있는 데이터 지우고 다 땡겨줘야 함 -> front를 밀기!
        front = (front + 2) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data


def deq():
    global front
    front = (front+1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
enq(6)
enq(7)
enq(8)
print(deq())
print(deq())
print(deq())
print(deq())


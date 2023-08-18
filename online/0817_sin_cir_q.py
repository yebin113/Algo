# n = 5 # queue 의 크기
#
# rear = front = -1
#
# my_q = [None] * 5  # queue 생성
#
#
# # addQ
# my_q[rear] = "A"
# rear += 1
#
# #deQ
# my_q[front] = None
# front += 1


class LinearQueue:
    def __init__(self, size):
        self.size = size # q 의 용량 초기화
        self.queue = [None] * size
        self.front = self.rear = -1

    # 포화 상태
    def is_full(self):
        return self.rear == self.size - 1


    # 공백 상태
    def is_empty(self):
        return self.front == -1 # front -1이면 q가 공백상태

    def enqueue(self, item):
        if self.is_full():
            print("현재 큐가 포화 상태 입니다.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = self.rear + 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("현재 큐가 비어이있습니다.")
            return None
        item = self.queue[self.front]  # front 위치의 아이템 추출
        if self.front == self.rear:
            self.front = self.rear = -1  # 큐에 아이템이 하나 남아있는 경우 front와 rear를 초기화
        else:
            self.front = self.front + 1  # front를 다음 위치로 이동
        return item

    def display(self):
        if self.is_empty():
            print("현재 출력할 요소가 없습니다.")
            return
        i = self.front
        while i != self.rear:  # front부터 rear까지 반복하면서 아이템 출력
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size  # 다음 위치로 이동
        print(self.queue[i], end=" ")  # rear 위치의 아이템 출력
        print()

queue = LinearQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # enQ에러 발생

queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()

queue.dequeue()  # deQ에러 발생

class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = 0


    def is_empty(self):
        if self.front == self.rear:
            return  True
        return False

    """
     큐의 시작과 끝이 연결되어있다. 
    큐의 포화상태를 판별하기 위해서 rear의 다음요소 % self.size 
    큐가 가득 찼다면,  (4 + 1) % 5  = 0 
     """
    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def enq(self, item):
        if self.is_full():
            raise Exception("Queue is Full!!!")
        self.rear = (self.rear + 1 ) % self.size
        self.queue[self.rear] = item

    def deq(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        self.front = (self.front + 1) % self.size
        return self.queue[self.front]
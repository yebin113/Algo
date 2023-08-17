n = 5   # 큐의 크기
rear = front = -1
my_q = [None] * n   # 큐 생성

# add Q
my_q[rear] = 'A'
rear += 1

# deQ
my_q[front] = None
front += 1

class LinearQueue:
    def __init__(self,size):
        self.size = size        # q의 용량 초기화
        self.queue = [None] * size
        self.front = self.rear = -1

    # 포화상태
    def is_full(self):
        return self.rear == self.size -1        #

    # 공백상태
    def is_empty(self):
        return self.front == 0   # front 가 -1이면 공백상태

    def enqueue(self,item):
        if self.is_full():  # 포화상태 체크
            print('포화상태')
            return

        # 공백 상태일때는 초기화
        elif self.is_empty():
            self.front = self.rear = -1
        self.rear = self.rear + 1       # rear의 값을 다음으로 이동
        self.queue[self.rear] = item


    def dequeue(self):
        if self.is_empty():
            print('큐가 빔')
            return None
        item = self.queue[self.front]       # front의 아이템 반환
        # deq 아이템 하나남은 경우 큐를 초기화 해준다
        if self.front == self.rear:

            self.front = self.rear = -1
        else:
            self.front = self.front + 1

        return item


class CircularQueue:
    def __init__(self,size):
        self.size = size        # q의 용량 초기화
        self.queue = [None] * size
        self.front = self.rear = 0      # 0으로 초기화

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    """
    큐의 시작과 끝이 연결되어잇다
     큐의 포화상태를 판별하기 위해서 rear의 다음요소 % self.size
     큐가 가득 찼다면, (4+1) % 5 == 0
     
    """

    def is_full(self):
        if (self.rear+1)% self.size == self.front:
            return True
        return False

    def enq(self,item):
        if self.is_full():
            # 경고문구 나오게하기
            raise Exception('Queue is full!!')
        self.rear = self.rear + 1 % self.size
        self.queue[self.rear] = item

    def deq(self):
        if self.is_empty():
            raise Exception('Queue is Empty')
        self.front = self.front + 1 % self.size
        return self.queue[self.front]

queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print(queue.queue)
print(queue.dequeue())
print(queue.queue)
print(queue.dequeue())
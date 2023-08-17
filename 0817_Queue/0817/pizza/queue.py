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
import heapq

class priorityQueue:
    def __init__(self):
        self.queue = []

        #  push
    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    # pop
    def pop(self):
        if self.queue:
            # 힙 구조를 유지시켜 주는것 == 우선순위 따라 줄을 세워놓는 것
            priority, item = heapq.heappop(self.queue)
        else:
            raise IndexError("큐가 비어있어요.")

pq = priorityQueue()

pq.push("task1", 1)
pq.push("task2", 2)
pq.push("task3", 3)
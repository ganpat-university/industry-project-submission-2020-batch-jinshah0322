import heapq

class DoubleEndedPriorityQueue:
    def __init__(self):
        self.min_heap = []  
        self.max_heap = []  

    def push_front(self, value):
        heapq.heappush(self.min_heap, value)

    def push_rear(self, value):
        heapq.heappush(self.max_heap, -value)

    def pop_front(self):
        if not self.min_heap:
            return None
        return heapq.heappop(self.min_heap)

    def pop_rear(self):
        if not self.max_heap:
            return None
        return -heapq.heappop(self.max_heap)


deque_pq = DoubleEndedPriorityQueue()

deque_pq.push_front(5)
deque_pq.push_rear(2)
deque_pq.push_front(8)

print("Front popped:", deque_pq.pop_front())  
print("Rear popped:", deque_pq.pop_rear())    

deque_pq.push_rear(3)
deque_pq.push_front(7)

print("Front popped:", deque_pq.pop_front())  
print("Rear popped:", deque_pq.pop_rear())    

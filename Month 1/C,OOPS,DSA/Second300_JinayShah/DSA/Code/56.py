import heapq

class DoubleEndedPriorityQueue:
    def __init__(self):
        self.min_heap = []  
        self.max_heap = []  

    def push(self, value):
        heapq.heappush(self.min_heap, value)
        heapq.heappush(self.max_heap, -value)

    def pop_front(self):
        if not self.min_heap:
            return None
        value = heapq.heappop(self.min_heap)
        self.max_heap.remove(-value)
        heapq.heapify(self.max_heap)
        return value

    def pop_rear(self):
        if not self.max_heap:
            return None
        value = -heapq.heappop(self.max_heap)
        self.min_heap.remove(value)
        heapq.heapify(self.min_heap)
        return value


deque_pq = DoubleEndedPriorityQueue()

deque_pq.push(5)
deque_pq.push(2)
deque_pq.push(8)

print("Front popped:", deque_pq.pop_front())  
print("Rear popped:", deque_pq.pop_rear())    

deque_pq.push(3)
deque_pq.push(7)

print("Front popped:", deque_pq.pop_front())  
print("Rear popped:", deque_pq.pop_rear())    

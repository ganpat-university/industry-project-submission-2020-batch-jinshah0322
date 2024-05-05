import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None 
    
    def is_empty(self):
        return len(self.heap) == 0

# Example usage:
if __name__ == "__main__":
    priority_queue = PriorityQueue()

    # Push elements with priorities
    priority_queue.push(3)
    priority_queue.push(1)
    priority_queue.push(4)
    priority_queue.push(2)

    # Pop elements with the highest priority
    while not priority_queue.is_empty():
        print(priority_queue.pop(), end=" ")
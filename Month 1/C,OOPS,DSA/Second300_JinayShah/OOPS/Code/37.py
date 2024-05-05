import threading
import ctypes

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HazardPointerManager:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.hazard_pointers = [None] * num_threads

    def acquire(self, thread_id, pointer):
        self.hazard_pointers[thread_id] = pointer

    def release(self, thread_id):
        self.hazard_pointers[thread_id] = None

    def get_hazard_pointers(self):
        return set(filter(None, self.hazard_pointers))

class LockFreeStack:
    def __init__(self):
        self.top = None
        self.hazard_pointer_manager = HazardPointerManager(num_threads=2)
        self.lock = threading.Lock()

    def push(self, value, thread_id):
        new_node = Node(value)

        while True:
            with self.lock:
                hazard_pointers = self.hazard_pointer_manager.get_hazard_pointers()

                if self.top in hazard_pointers:
                    continue  # Retry if top is a hazard pointer

                new_node.next = self.top
                self.hazard_pointer_manager.acquire(thread_id, self.top)

                if self.top == self.hazard_pointer_manager.get_hazard_pointers():
                    self.top = new_node
                    self.hazard_pointer_manager.release(thread_id)
                    return

    def pop(self, thread_id):
        while True:
            with self.lock:
                hazard_pointers = self.hazard_pointer_manager.get_hazard_pointers()

                if self.top in hazard_pointers:
                    continue  # Retry if top is a hazard pointer

                self.hazard_pointer_manager.acquire(thread_id, self.top)

                if self.top == self.hazard_pointer_manager.get_hazard_pointers():
                    if self.top is None:
                        self.hazard_pointer_manager.release(thread_id)
                        return None  # Stack is empty
                    else:
                        value = self.top.value
                        self.top = self.top.next
                        self.hazard_pointer_manager.release(thread_id)
                        return value

def worker(stack, thread_id):
    for i in range(5):
        stack.push(i, thread_id)
        value = stack.pop(thread_id)
        print(f"Thread {thread_id}: Popped {value}")

if __name__ == "__main__":
    stack = LockFreeStack()

    thread1 = threading.Thread(target=worker, args=(stack, 0))
    thread2 = threading.Thread(target=worker, args=(stack, 1))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

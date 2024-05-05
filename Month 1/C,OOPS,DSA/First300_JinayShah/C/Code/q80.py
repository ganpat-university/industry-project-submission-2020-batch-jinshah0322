import threading
import queue
import time
import random

buffer = queue.Queue(maxsize=5)

num_items = 10

def producer():
    for _ in range(num_items):
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"Produced {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    for _ in range(num_items):
        item = buffer.get()
        print(f"Consumed {item}")
        time.sleep(random.uniform(0.1, 0.5))

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Production and consumption completed.")

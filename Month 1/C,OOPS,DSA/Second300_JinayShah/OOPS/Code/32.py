import queue
import threading
import time

def producer(queue, items):
    for item in items:
        print(f"Producing: {item}")
        queue.put(item)
        time.sleep(0.1)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming: {item}")
        time.sleep(0.2)

if __name__ == "__main__":
    shared_queue = queue.Queue()

    producer_thread = threading.Thread(target=producer, args=(shared_queue, range(5)))
    consumer_thread = threading.Thread(target=consumer, args=(shared_queue,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    shared_queue.put(None) 
    consumer_thread.join()
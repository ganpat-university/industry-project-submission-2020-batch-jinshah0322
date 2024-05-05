import queue
import threading

q = queue.Queue()

def producer():
    for i in range(10):
        q.put(i)
        print('Produced: ', i)

def consumer():
    while not q.empty():
        item = q.get()
        print('Consumed: ', item)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

import threading
import queue
import time

def worker(queue):
    while True:
        task = queue.get()
        if task is None:
            break

        task_function(task)
        queue.task_done()

def task_function(task_id):
    print(f"Task {task_id} started.")
    time.sleep(2)
    print(f"Task {task_id} completed.")

num_tasks = 5

task_queue = queue.Queue()

num_workers = 2
workers = [threading.Thread(target=worker, args=(task_queue,)) for _ in range(num_workers)]

for worker_thread in workers:
    worker_thread.start()

for i in range(num_tasks):
    task_queue.put(i)

task_queue.join()

for _ in range(num_workers):
    task_queue.put(None)

for worker_thread in workers:
    worker_thread.join()

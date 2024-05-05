import threading
class LockFreeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            self.value += 1
    def get_value(self):
        return self.value

def increment_counter(counter, transactions):
    for _ in range(transactions):
        counter.increment()
if __name__ == "__main__":
    num_threads = 4
    transactions_per_thread = 100000
    counter = LockFreeCounter()
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=increment_counter, args=(counter, transactions_per_thread))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Final Counter Value (Lock-Free):", counter.get_value())
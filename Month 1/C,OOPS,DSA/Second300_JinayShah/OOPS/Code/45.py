import multiprocessing
import numpy as np

def worker_function(data_chunk, result_queue):
    local_sum = np.sum(data_chunk)
    result_queue.put(local_sum)

def main():
    array_size = 1000000
    data = np.random.randint(1, 10, array_size)

    num_processes = 4
    chunk_size = len(data) // num_processes
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    result_queue = multiprocessing.Queue()

    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=worker_function, args=(chunk, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    print("Total sum:", total_sum)

if __name__ == "__main__":
    main()

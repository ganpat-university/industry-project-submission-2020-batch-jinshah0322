import concurrent.futures

def add_vectors_parallel(a, b):
    result = [0] * len(a)

    def add_element(i):
        result[i] = a[i] + b[i]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(add_element, range(len(a)))

    return result

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]

    result = add_vectors_parallel(a, b)

    print("Vector A:", a)
    print("Vector B:", b)
    print("Result:", result)
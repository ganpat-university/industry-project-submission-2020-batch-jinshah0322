import threading

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        t1 = threading.Thread(target=mergeSort, args=(lefthalf,))
        t2 = threading.Thread(target=mergeSort, args=(righthalf,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i + 1
            else:
                arr[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j + 1
            k = k + 1

data = [1, 9, 3, 7, 5, 2, 6, 4, 8]
mergeSort(data)
print(data)
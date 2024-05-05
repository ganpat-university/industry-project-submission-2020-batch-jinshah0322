def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

def quicksort(arr,low,high):
    if(low<high):
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
quicksort(arr,0,len(arr)-1)
print(arr)
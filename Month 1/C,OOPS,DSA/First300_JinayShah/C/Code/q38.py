def mergesort(arr):
    if(len(arr)>1):
        mid = int(len(arr)/2)
        left = arr[0:mid]
        right = arr[mid:len(arr)]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if(left[i]<right[j]):
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            k+=1
            j+=1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
mergesort(arr)
print(arr)
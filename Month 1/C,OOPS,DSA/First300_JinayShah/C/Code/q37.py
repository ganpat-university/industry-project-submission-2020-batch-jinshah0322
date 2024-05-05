def sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    return arr

def binarysearch(arr,left,right,element):
    arr = sort(arr)
    mid = int((left+right)/2)
    if(element==arr[mid]):
        print(f"Element found at index {mid}")
    elif(element>arr[mid]):
         binarysearch(arr,mid+1,right,element)
    elif(element<arr[mid]):
         binarysearch(arr,left,mid-1,element)

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
element = int(input())
binarysearch(arr,0,len(arr)-1,element)
print(arr)
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
element = int(input())
for i in range(len(arr)):
    if(element==arr[i]):
        print(f"element found at {i} index")
        break   
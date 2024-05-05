arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
intersection = []


for i in range(len(arr1)):
    if(arr1[i] in arr2):
        intersection.append(arr1[i])

print(intersection)
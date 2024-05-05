queue = list(map(int,input("Enter elements of queue:").split()))
k = int(input("Enter value of k:"))

for i in range(0,k):
    queue.append(queue.pop(0))

print(queue)
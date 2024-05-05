def insert(queue,element):
    queue.append(element)

def remove(queue):
    print(f"Removed element is {queue.pop(0)}")

def traverse(queue):
    print(queue)

queue = []
n = int(input())
for i in range(n):
    insert(queue,input())
traverse(queue)
remove(queue)
traverse(queue)
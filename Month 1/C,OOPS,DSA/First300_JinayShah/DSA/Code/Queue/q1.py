def insert(element,queue):
    queue.append(element)

def remove(queue):
    queue.pop(0)

queue = []
condition = True
while(condition):
    statement = input("Do you want to insert element to queue\n1)Yes\n2)No:").lower()
    if(statement=="yes" or statement=="y" or statement=="1"):
        element = int(input("Enter element to insert to queue:"))
        insert(element,queue)
    else:
        condition=False
print(queue)
condition = True
while(condition):
    statement = input("Do you want to remove element from queue\n1)Yes\n2)No:").lower()
    if(statement=="yes" or statement=="y" or statement=="1"):
        remove(queue)
    else:
        condition=False
print(queue)
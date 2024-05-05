class priorityQueue:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self,element):
        self.queue.append(element)

    def delete(self):
        maxValue = 0
        for i in range(len(self.queue)):
            if(self.queue[i]>self.queue[maxValue]):
                maxValue=i
        item = self.queue[maxValue]
        del self.queue[maxValue]
        return item
    
myQueue = priorityQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(7)
# print(myQueue)            
while not myQueue.isEmpty():
    print(myQueue.delete()) 
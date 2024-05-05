class myQueue:
    def __init__(self,cap):
        self.l = [None]*cap
        self.capacity = cap
        self.size = 0
        self.front = 0

    def enqueue(self,x):
        if self.size == self.capacity:
            return
        else:
            rear = (self.front+self.size-1)%self.capacity
            rear = (rear+1)%self.capacity
            self.l[rear] = x
            self.size+=1

    def dequeue(self,x):
        if(self.size == 0):
            return
        else:
            res = self.l[self.front]
            self.front = (self.front+1)%self.capacity
            self.size = self.size-1
            return res  
        
    def display(self):
        print(self.l)

q = myQueue(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue(10)
q.dequeue(20)
q.dequeue(30)
q.dequeue(40)
q.enqueue(50)
q.display()
class myQueue:
    def __init__(self) :
        self.queue = []
        self.min_arr = []

    def push(self,element):
        if(len(self.min_arr)==0):
            self.min_arr.append(element)
            return self.queue.append(element)
        else:
            if(self.min_arr[-1]>=element):
                self.min_arr.append(element)
            return self.queue.append(element)

    def pop(self):
        print(f"Popped element is {self.queue.pop(0)}")

    def top(self):
        if(len(self.queue)>0):
            print(f"Top element is {self.queue[-1]}")
        else:
            return

    def traverse(self):
        print(self.queue)

    def minElement(self):
        print(self.min_arr[-1])

n = int(input())
queue = myQueue()
for i in range(n):
    queue.push(input())
queue.traverse()
queue.pop()
queue.traverse()
queue.top()
queue.minElement()
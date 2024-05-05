import random

class Node:
   def __init__(self, key, value, height):
       self.key = key
       self.value = value
       self.height = height
       self.forward = [None]*height

class SkipList:
   def __init__(self):
       self.head = Node(float('-inf'), float('-inf'), 16)
       self.level = 0

   def insert(self, key, value):
       update = [None]*16
       x = self.head
       for i in range(self.level, -1, -1):
           while x.forward[i] and x.forward[i].key < key:
               x = x.forward[i]
           update[i] = x

       level = self.randomLevel()
       if level > self.level:
           for i in range(self.level, level):
               update[i] = self.head
           self.level = level

       x = Node(key, value, level)
       for i in range(level):
           x.forward[i] = update[i].forward[i]
           update[i].forward[i] = x

   def delete(self, key):
       update = [None]*16
       x = self.head
       for i in range(self.level, -1, -1):
           while x.forward[i] and x.forward[i].key < key:
               x = x.forward[i]
           update[i] = x

       if x.forward[0] and x.forward[0].key == key:
           for i in range(self.level):
               if update[i].forward[i] != x.forward[i]:
                  break
               update[i].forward[i] = x.forward[i]
           del x

   def search(self, key):
       x = self.head
       for i in range(self.level, -1, -1):
           while x.forward[i] and x.forward[i].key < key:
               x = x.forward[i]
       if x.forward[0] and x.forward[0].key == key:
           return x.forward[0].value
       return None

   def randomLevel(self):
       level = 1
       while random.randint(0, 1):
           level += 1
       return level

# Driver Code
sl = SkipList()
sl.insert(1, "one")
sl.insert(2, "two")
sl.insert(3, "three")
print(sl.search(1))     
print(sl.search(2))     
print(sl.search(3))     
print(sl.search(4))     

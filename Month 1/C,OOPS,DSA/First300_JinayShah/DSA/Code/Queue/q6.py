from collections import deque

fruits = ["apple","mango","banana","grapes"]
queue = deque(fruits)
print(queue)
print(queue.pop())
print(queue.popleft())
print(queue)
queue.appendleft("Watermelon")
print(queue)
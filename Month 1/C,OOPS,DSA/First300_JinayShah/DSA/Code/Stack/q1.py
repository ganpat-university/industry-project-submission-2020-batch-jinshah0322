def push(stack,element):
    stack.append(element)

def pop(stack):
    print(f"Popped element is {stack.pop()}")

def traverse(stack):
    print(stack)

stack = []
n = int(input())
for i in range(n):
    push(stack,input())
traverse(stack)
pop(stack)
traverse(stack)
def evaluate(expression):
    stack = []
    for i in range(len(expression)):
        element = expression[i]
        if(element.isdigit()):
            stack.append(element)
        else:
            element1=stack.pop()
            element2 = stack.pop()
            stack.append(str(eval(element2 + element + element1)))
    print(stack.pop())

expression = input()
evaluate(expression)
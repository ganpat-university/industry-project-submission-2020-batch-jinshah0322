def precedence(operator):
    if(operator=='*' or operator=='/'):
        return 2
    elif(operator=='+' or operator=='-'):
        return 1
    else:
        return -1
    
def infixToPostfix(expression):
    answer=[]
    stack=[]
    for i in range(len(expression)):
        element = expression[i]
        if(('a'<= element <= 'z') or ('A'<=element<='Z') or ('0'<=element<='9')):
            answer.append(element)
        elif(element=='('):
            stack.append('(')
        elif(element==')'):
            while(stack and stack[-1]!='('):
                answer.append(stack.pop())
            stack.pop()
        else:
            while(stack and ((precedence(element)<precedence(stack[-1])) or (precedence(element) == precedence(stack[-1])))):
                answer.append(stack.pop())
            stack.append(element)
    while stack:
        answer.append(stack.pop())
    print(''.join(answer))

expression = input()
infixToPostfix(expression)
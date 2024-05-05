openparenthesis = ['[','{','(']
closeparenthesis = [']','}',')']

def checkParenthesis(expression):
    stack = []
    for i in range(len(expression)):
        if(expression[i] in openparenthesis):
            stack.append(expression[i])
        elif(expression[i] in closeparenthesis):
            position = closeparenthesis.index(expression[i])
            if(len(stack)>0 and stack[-1] == openparenthesis[position]):
                stack.pop()
            else:
                return "Parenthesis are not balanced"
    if(len(stack)>0):
        return "Parenthesis are not balanced"
    else:
        return "Parenthesis are balanced"


expression = input()
print(checkParenthesis(expression))
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

class Context:
    def __init__(self):
        self.variables = {}

context = Context()
expression = Add(Number(5), Subtract(Number(10), Number(3)))
result = expression.interpret(context)
print(f"Result: {result}")

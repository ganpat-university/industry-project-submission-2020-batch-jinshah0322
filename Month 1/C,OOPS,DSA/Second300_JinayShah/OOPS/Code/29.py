class Expression:
    def eval(self):
        raise NotImplementedError

class Vector(Expression):
    def __init__(self, data):
        self.data = data

    def eval(self):
        return self.data

class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        left_value = self.left.eval()
        right_value = self.right.eval()
        return [x + y for x, y in zip(left_value, right_value)]

vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])

expression = AddExpression(vector1, vector2)

result = expression.eval()

print("Vector 1:", vector1.eval())
print("Vector 2:", vector2.eval())
print("Result:", result)

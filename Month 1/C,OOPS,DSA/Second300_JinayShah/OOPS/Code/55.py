class DSLContext:
    def __init__(self):
        self.variables = {}

    def assign(self, variable, value):
        self.variables[variable] = value

    def evaluate(self, expression):
        return eval(expression, {}, self.variables)

def math_dsl():
    context = DSLContext()

    def let(variable, value):
        context.assign(variable, value)

    def calculate(expression):
        return context.evaluate(expression)

    return let, calculate

let, calculate = math_dsl()

let("x", 5)
let("y", 10)

result = calculate("x + y * 2")
print("Result:", result)

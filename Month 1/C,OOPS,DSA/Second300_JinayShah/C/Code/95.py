class Token:
    def __init__(self, bindings=None):
        self.bindings = bindings if bindings is not None else {}

    def clone(self):
        return Token(self.bindings.copy())


class AlphaMemory:
    def __init__(self):
        self.tokens = []

    def add_token(self, token):
        self.tokens.append(token)

    def remove_token(self, token):
        self.tokens.remove(token)


class BetaMemory:
    def __init__(self, parent=None):
        self.parent = parent
        self.tokens = []

    def add_token(self, token):
        self.tokens.append(token)


class ProductionNode:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action


class ReteNetwork:
    def __init__(self):
        self.alpha_memory = {}
        self.beta_memory = []
        self.production_nodes = []

    def add_production_node(self, production_node):
        self.production_nodes.append(production_node)

    def add_alpha_memory(self, condition):
        alpha_memory = AlphaMemory()
        self.alpha_memory[condition] = alpha_memory
        return alpha_memory

    def find_or_create_alpha_memory(self, condition):
        if condition in self.alpha_memory:
            return self.alpha_memory[condition]
        else:
            return self.add_alpha_memory(condition)

    def find_or_create_beta_memory(self, parent_beta_memory):
        for beta_memory in self.beta_memory:
            if beta_memory.parent == parent_beta_memory:
                return beta_memory
        new_beta_memory = BetaMemory(parent_beta_memory)
        self.beta_memory.append(new_beta_memory)
        return new_beta_memory

    def activate_node(self, condition, token):
        alpha_memory = self.find_or_create_alpha_memory(condition)
        alpha_memory.add_token(token)
        for beta_memory in self.beta_memory:
            self.join_beta_alpha(beta_memory, alpha_memory, token)

    def join_beta_alpha(self, beta_memory, alpha_memory, token):
        new_token = token.clone()
        new_token.bindings.update(alpha_memory.tokens[-1].bindings)
        beta_memory.add_token(new_token)
        for production_node in self.production_nodes:
            if production_node.condition.check(new_token.bindings):
                production_node.action.execute(new_token.bindings)


class Condition:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def check(self, bindings):
        return self.attribute in bindings and bindings[self.attribute] == self.value


class Action:
    def __init__(self, name):
        self.name = name

    def execute(self, bindings):
        print(f"Action '{self.name}' executed with bindings: {bindings.bindings}")



rete_network = ReteNetwork()

condition1 = Condition("color", "red")
condition2 = Condition("shape", "circle")
condition3 = Condition("size", "large")

action1 = Action("Action1")
action2 = Action("Action2")
action3 = Action("Action3")

production_node1 = ProductionNode(condition1, action1)
production_node2 = ProductionNode(condition2, action2)
production_node3 = ProductionNode(condition3, action3)

rete_network.add_production_node(production_node1)
rete_network.add_production_node(production_node2)
rete_network.add_production_node(production_node3)

token1 = Token({"color": "red"})
token2 = Token({"shape": "circle"})
token3 = Token({"size": "large"})

rete_network.activate_node(condition1, token1)
rete_network.activate_node(condition2, token2)
rete_network.activate_node(condition3, token3)

action1.execute(token1)
action2.execute(token2)
action3.execute(token3)
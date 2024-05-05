class VendingMachineContext:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()

class NoCoinState:
    def handle(self):
        print("No coin in vending machine")

class HasCoinState:
    def handle(self):
        print("There is a coin in vending machine")

traffic_light = VendingMachineContext()

traffic_light.set_state(NoCoinState())

traffic_light.request()

traffic_light.set_state(HasCoinState())
traffic_light.request()
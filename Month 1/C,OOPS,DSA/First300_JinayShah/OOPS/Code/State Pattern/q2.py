class VendingMachineContext:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()

class StateA:
    def handle(self):
        print("This is state A")

class StateB:
    def handle(self):
        print("This is state B")

traffic_light = VendingMachineContext()

traffic_light.set_state(StateA())

traffic_light.request()

traffic_light.set_state(StateB())
traffic_light.request()
class TrafficLightContext:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()

class RedState:
    def handle(self):
        print("Traffic Light is Red")

class YellowState:
    def handle(self):
        print("Traffic Light is Yellow")

class GreenState:
    def handle(self):
        print("Traffic Light is Green")

traffic_light = TrafficLightContext()

traffic_light.set_state(RedState())

traffic_light.request()

traffic_light.set_state(YellowState())
traffic_light.request()

traffic_light.set_state(GreenState())
traffic_light.request()
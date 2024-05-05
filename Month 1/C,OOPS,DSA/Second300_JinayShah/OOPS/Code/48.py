class TextElement:
    def __init__(self, content):
        self.content = content

    def render(self):
        print(self.content)

class ButtonElement:
    def __init__(self, label):
        self.label = label

    def render(self):
        print(f"[{self.label}]")
def render_elements(elements):
    for element in elements:
        element.render()
ui_elements = [
    {'type': 'TextElement', 'content': 'Hello, world!'},
    {'type': 'ButtonElement', 'label': 'OK'}
]

objects = []
for element in ui_elements:
    cls = globals()[element['type']]
    obj = cls(**{k: v for k, v in element.items() if k != 'type'})
    objects.append(obj)

render_elements(objects)

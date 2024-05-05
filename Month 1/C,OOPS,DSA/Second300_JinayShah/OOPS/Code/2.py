# Originator: The object whose state needs to be saved
class TextEditor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def save_state(self):
        return TextEditorMemento(self.content)

    def restore_state(self, memento):
        self.content = memento.get_saved_state()

    def display_content(self):
        print(f"Current Content: {self.content}")


# Memento: The object that stores the state of the originator
class TextEditorMemento:
    def __init__(self, content):
        self.saved_state = content

    def get_saved_state(self):
        return self.saved_state


# Caretaker: Manages and keeps track of the mementos
class History:
    def __init__(self):
        self.states = []

    def add_state(self, memento):
        self.states.append(memento)

    def get_state(self, index):
        return self.states[index]



editor = TextEditor()
history = History()

editor.display_content()

editor.write("Hello, ")
editor.display_content()

history.add_state(editor.save_state())

editor.write("world!")
editor.display_content()

editor.restore_state(history.get_state(0))
editor.display_content()
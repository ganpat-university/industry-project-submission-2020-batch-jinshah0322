class Character:
    def __init__(self, symbol, font_size, color):
        self.symbol = symbol
        self.font_size = font_size
        self.color = color

    def display(self):
        print(f"Symbol: {self.symbol}, Font Size: {self.font_size}, Color: {self.color}")

class CharacterFactory:
    _characters = {}

    @classmethod
    def get_character(cls, symbol, font_size, color):
        key = (symbol, font_size, color)
        if key not in cls._characters:
            cls._characters[key] = Character(symbol, font_size, color)
        return cls._characters[key]

class Text:
    def __init__(self):
        self.characters = []

    def add_character(self, symbol, font_size, color):
        character = CharacterFactory.get_character(symbol, font_size, color)
        self.characters.append(character)

    def display(self):
        for character in self.characters:
            character.display()

text = Text()
text.add_character("A", 12, "Black")
text.add_character("B", 12, "Red")
text.add_character("A", 12, "Black")  # Reusing existing 'A' character
text.display()
class text:
    def textType(self):
        return "normal text"
    
class Bold:
    def __init__(self,text) -> None:
        self.text = text

    def textType(self):
        return self.text.textType() + " converted to bold"
    
class Italic:
    def __init__(self,text):
        self.text = text

    def textType(self):
        return self.text.textType() + " converted to italic"
    
c = text()
print(c.textType())
b = Bold(c)
print(b.textType())
i = Italic(c)
print(i.textType())
import zope.interface

class Document(zope.interface.Interface):
    def print(self):
        pass

@zope.interface.implementer(Document)
class PDFDocument:
    def print(self):
        print("this is a pdf document")


@zope.interface.implementer(Document)
class WordDocument:
    def print(self):
        print("This is word document")

class documentFactory:
    def __init__(self,doc) :
        self.doc = doc
    def documentType(self):
        if(self.doc=="word"):
            WordDocument().print()
        elif(self.doc=="pdf"):
            PDFDocument().print()
        else:
            print("Invalid document type")
    
doc = input("Enter document type:").lower()
docfactory = documentFactory(doc)
docfactory.documentType()
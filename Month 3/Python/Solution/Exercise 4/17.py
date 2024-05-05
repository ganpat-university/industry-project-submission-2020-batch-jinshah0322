class myClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b

obj = myClass(1,2)

print(hasattr(obj,'a'))

print(getattr(obj,'a'))

setattr(obj,'a',3)
print(getattr(obj,'a'))

delattr(obj,'a')
print(hasattr(obj,'a'))
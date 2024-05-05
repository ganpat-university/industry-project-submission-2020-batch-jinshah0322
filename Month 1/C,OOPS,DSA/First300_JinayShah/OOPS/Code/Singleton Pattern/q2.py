class Logger:
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Logger,cls).__new__(cls)
        return cls.instance
    
    def log(self,message):
        print(message)

obj = Logger()
obj.log("This is singleton object")

obj1 = Logger()
obj1.log("This is another object")

if(obj==obj1):
    print("There is only one object of class which is singleton object")
file = open("python.txt","r")
code = file.read()
file.close()
try:
    exec(code)
except:
    print("Invalid code")
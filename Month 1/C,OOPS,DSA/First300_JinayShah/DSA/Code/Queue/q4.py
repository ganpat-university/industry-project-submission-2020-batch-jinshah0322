n = int(input("Enter n:"))
binary = []
subBinary = ''
for i in range(n+1):
    if(i==0):
        subBinary+='0'
    while(i>0):
        subBinary+=str(i%2)
        i=i//2
    binary.append(subBinary[::-1])
    subBinary=''

print(binary)
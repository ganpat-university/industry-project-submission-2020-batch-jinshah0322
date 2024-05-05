def read(file):
    print("\nReading the file")
    print(file.read())

def write(file):
    print("\nWriting in file")
    file.write("Writing content to file\n")
    file.seek(0)
    read(file)

def copy(file1,file2):
    print("\nCopying the content from one file to another")
    file1.seek(0)
    readedContent = file1.read()
    file2.write(readedContent)
    file2.seek(0)
    print(file2.read())

file = open("q73read.txt",'r')
read(file)

file1 = open("q73write.txt",'w+')
write(file1)

file2 = open("q73copy.txt",'w+')
copy(file,file2)
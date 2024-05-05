file = open("test_file.data","wb")
binary_data = bytearray([0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x57, 0x6F, 0x72, 0x6C, 0x64])
file.write(binary_data)
file.close()

file = open("test_file.data","rb")
print(file.read())
file.close()
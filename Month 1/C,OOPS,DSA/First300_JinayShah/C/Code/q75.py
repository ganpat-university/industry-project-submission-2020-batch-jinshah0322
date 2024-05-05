def memoryAllcation(x):
    print(x)
    y = x
    print(y)
    if(id(x) == id(y)):
        print("Both x and y reference to same object")
    else:
        print("Both x and y reference to different objects")
    x+="shah"
    print(f"\n{x}")
    print(y)
    if(id(x) == id(y)):
        print("Both x and y reference to same object")
    else:
        print("Both x and y reference to different objects")
    print("\nDeallocating the memory")
    del(x)
    del(y)
    # print(x)
    # print(y)
x = input("Enter your name:")
memoryAllcation(x)


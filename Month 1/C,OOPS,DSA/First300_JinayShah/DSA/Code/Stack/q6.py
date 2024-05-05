def TOH(n,a,b,c):
    if(n==1):
        print(f"Move 1st disk from {a} to {c}")
        return 
    TOH(n-1,a,c,b)
    print(f"Move {n}th disk from {a} to {c}")
    TOH(n-1,b,a,c)

n = int(input("Enter number of discs:"))
TOH(n,'A','C','B')
def prime():
    prime_num = []
    for i in range(2,101):
        count=0
        for j in range(2,i):
            if(i%j==0):
                count+=1
                break
        if(not count>0):
            prime_num.append(i)
            count=0
            yield i

primeNums = prime()
for i in primeNums:
    print(i,end=" ")
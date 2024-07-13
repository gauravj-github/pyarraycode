n=4
k=1
for i in range(1,n):
    for j in range(i):
        print(k,end="")
        k+=1
    print()
    
p=k-1
for i in range(1,n):
    for j in range(n-i):
        print(p,end="")
        p-=1
    print()



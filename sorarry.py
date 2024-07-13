l=[1,2,0,44]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp 
        print(l)
a=[10,20,70,90,80,20,20,20,20,10]

for i in range(len(a)):
    c=0
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            c+=1
        if c>1:
            break
    if c==1:
        print(a[i])
    
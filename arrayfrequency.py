a=[10,30,10,20,10,20,30,10,1]

c={}

for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)




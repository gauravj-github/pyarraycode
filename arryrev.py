a=[10,20,30,40,50,60,20]
c=[] 

for i in range(len(a)-1,-1,-1):
    print(i)
    c.append(a[i])
print(c)
l=[2,3,44,2,55,8,9,1]
m=l[0]
for i in range(len(l)):
    if l[i]<m:
        m=l[i]
        print(m)

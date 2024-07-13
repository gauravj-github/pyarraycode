a = [1,3,-1,4,-3,-5,-6,3,7]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
            m=a[i]
            a[i]=a[j]
            a[j]=m
print(a)
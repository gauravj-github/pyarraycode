a=[1,4,2,6,5,7,8,3]


for i in range(len(a)):
    for j in range(len(a)):
        if a[i]>a[j]:
            m=a[i]
            a[i]=a[j]
            a[j]=m
print(a)


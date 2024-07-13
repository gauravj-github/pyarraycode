arry1=[1,2,0,44]

for i in range(len(arry1)):
    for j in range(i+1,len(arry1)):
        if arry1[i]>arry1[j]:
            tem=arry1[i]
            arry1[i]=arry1[j]
            arry1[j]=tem
        print(arry1)
print(arry1[1])

    
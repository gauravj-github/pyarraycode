array = [5,2,3,4,1,6,7]
sum=7

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j] == sum:
            print(array[i],array[j])
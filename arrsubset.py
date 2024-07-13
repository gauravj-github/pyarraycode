a = [11,12,13,21,30,70]
b=[11,30,70,12]
c=0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c+=1
    
if j==c:
    print("arr2 is subset of arr1") 
else:
    print("arr2 is not subset of arr1")
             


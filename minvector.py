'''convert a1 array in assending order '''
a1=[1,2,6,3,7]
'''convert a1 array in d order '''
a2=[10,7,45,3,7]
n=len(a1)
product=0

for i in range(len(a1)):
    for j in range(i+1):
        if a1[i]<a1[j]:
            temp=a1[i]
            a1[i]=a1[j]
            a1[j]=temp
print(a1)
            

for i in range(len(a1)):
    for j in range(i+1):
        if a2[i]>a2[j]:
            temp=a2[i]
            a2[i]=a2[j]
            a2[j]=temp
print(a2)
            
for i in range(n):
    product+=a1[i]*a2[i]
print(product)

a1=[1,2,6,3,7]
a2=[10,7,45,3,7]

n=len(a1)

produt=0

for i in range(n):
  for j in range(i+1):
     if a1[i]>a1[j]:
        tem=a1[i]
        a1[i]=a1[j]
        a1[j]=tem
print(a1)

for i in range(n):
  for j in range(i+1):
     if a2[i]>a2[j]:
        tem=a2[i]
        a2[i]=a2[j]
        a2[j]=tem
print(a2)

for i in range(n):
    produt+=a1[i]*a2[j]
print(produt) 
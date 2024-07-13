a=[1,2,3,34,4,5,6]
m=a[0]
l=a[0]

for i in range(len(a)):
    if m>a[i] :
        m=a[i]
       
    if l<a[i]:
        l=a[i]
print(m)
print(l)
a=[0,2,0,3,0,5,6,7,8,9]
n=len(a)
for i in range(n):
 for j in range(n):

    if a[i]>a[j]:
      temp = a[i]
      a[i] = a[j]
      a[j] = temp
      print(a)




n=input("enter any srting")
k=""

for i in range(len(n)-1,-1,-1):
     print(i)
     k+=n[i]
print(k)
print(len(n))
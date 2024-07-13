a = [1,2,3,4]
b = [4,5,6,7,]

for i in a:
  for j in b:
    if i==j:
      print(i)


for j in range (len(b)):
    if b[j] not in a:
      a.append(b[j])
print(a)



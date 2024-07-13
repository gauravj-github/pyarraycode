str=input("enter any value")
count=0
for i in str:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E' or i=='I' or i=='U':
        count+=1
if count==0:
    print("no vowel in str")
else:
  print(count)
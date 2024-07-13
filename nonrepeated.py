s='prepinsta'
r=''


for i in s:
    count=0
    for j in s:
        if i==j :
            count+=1

        if count>1:
            break

    if count==1:
       r=r+i
print(r)
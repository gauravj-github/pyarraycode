a=[10,20,70,90,80,20,10,20]

for i in a:
    c=0
    for j in a:
        if i==j:
           c+=1
        if c>1:
            break
    if c==1:
        print(i)
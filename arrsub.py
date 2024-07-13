a =[11,12,13,21,30,70]
b = [11,30,70,12]
c=len(b)
d=0
for i in a:

    for j in range(c):
        if i==b[j]:
            d+=1
            break
if d==c:
    print("arry2[] is subset of arry1[]")
else:

    print("arry2[] is not subset of arry1[]")

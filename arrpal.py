a = [1, 232, 5545455, 909090, 161, 321]
d = []

for num in a:
    reversed_num = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        reversed_num = (reversed_num * 10) + digit
        temp = temp // 10
    if reversed_num in a:
        d.append(reversed_num)
    m=d[0]
    for i in range(len(d)):
        
        if d[i]>m:
            m=d[i]
print(m)
            
    


s="(x+y)+(z+q)"
e=""

for i in s:
    if ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125:
       pass
    else:
        e=e+i
print(e)
  
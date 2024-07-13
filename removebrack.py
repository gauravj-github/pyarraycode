s="(xy+yty"
a=['(',')','{','}','[',']']
for i in s:
    if i in a:
        s=s.replace(i,'')
print(s)
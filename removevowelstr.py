a=input("enret any string")

l=['A','E','I','O','U','a','e','i','o','u']

for i in a:
    if i in l:
        a=a.replace(i,"")
        print(a)
n=input("enter any character")
l=['A','E','I','O','U','a','e','i','o','u']
for i in range(len(l)):
 print(i)
 if n==l[i]:
     print("it is vowel " +n)
     break
else:
    print("consonant")
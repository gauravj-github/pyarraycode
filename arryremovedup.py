def remove_duplicates(dup):
    nondup=[]
    for i in dup:
        if i not in nondup:
            nondup.append(i)
    print(nondup)

data=[10,20,30,30,40,50,50,60,70]
remove_duplicates(data)
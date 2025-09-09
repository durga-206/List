def remove(li,new):
    for i in li:
        if i not in new:
            new.append(i)
    return new
li=input().split()
new=[]
print(remove(li,new))

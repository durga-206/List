li=input().split()
sort=[]
temp=0
for i in li:
    a=int(i)
    b=int(i)+1
    if a>b:
        temp=a
        a=b
        b=temp
        sort.append(temp)
print(sort)

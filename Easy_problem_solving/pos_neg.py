li=input().split()
pos=[]
neg=[]
for i in li:
    if int(i)>0:
        pos.append(int(i))
    elif int(i)<0:
        neg.append(int(i))
print(f"{pos} are positive numbers,{neg} are negative numbers")

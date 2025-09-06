li=input().split()
new1=[]
new2=[]
for i in li:
     if int(i)==0: 
            new1.append(int(i))           
     else:
            new2.append(int(i))          
print(new2+new1)

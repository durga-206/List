'''li=input().split()
new1=[]
new2=[]
for i in li:
     if int(i)==0: 
            new1.append(int(i))           
     else:
            new2.append(int(i))          
print(new2+new1)'''
def zero_End(li):
     new1=[]
     new2=[]
     for i in li:
      if int(i)==0: 
            new1.append(int(i))           
      else:
            new2.append(int(i))          
     return new2+new1
li=input().split()
print(zero_End(li))

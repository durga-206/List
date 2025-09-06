li=[1,2,3,4,5,1,2,2,3,3,4,4,4,4,5,5]
count=[]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
           print(li[i],li[j])
print(count)
'''def majority(li):
   count=[] 
   for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
           print(li[i],li[j])
    return count
li=input().split()
print(majority(li))'''

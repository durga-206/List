def second_large(li):
 for i in range(len(li)):
   for j in range(i+1,len(li)):
       if li[i]<li[j]:
           li[i],li[j]=li[j],li[i]
 return li[1]
li=input().split()
print(second_large(li))

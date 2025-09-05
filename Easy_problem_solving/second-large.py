li=[5,1,0,3]
for i in range(len(li)):
   for j in range(i+1,len(li)):
       if li[i]<li[j]:
           li[i],li[j]=li[j],li[i]
print(li[1])
       #print(f"i={i} and j={j}")



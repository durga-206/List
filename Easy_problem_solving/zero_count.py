def zero_Count(li):
 count=0
 for i in li:
    if int(i)==0:
        count+=1
 return count
li=input().split()
print(zero_Count(li))

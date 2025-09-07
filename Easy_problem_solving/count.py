def counts(lis,target):
 count=0 
 for i in lis:
    if int(i)==target:
        count+=1
 return count
lis=input().split()
target=int(input('Enter the target element:'))
print(counts(lis,target))



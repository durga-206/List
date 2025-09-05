li=input().split()
#li=[5,2000,4,2]
maxi=int(li[0])
for i in li:
    if maxi<int(i):
        maxi=int(i)
print(maxi)

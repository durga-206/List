li=input().split()
#n=int(li[len(li)-1])
n=int(max(li))
for i in range(1,n+1):
    if str(i) not in li:
        print(i,end=' ')
print('n=',n)

def mis_Element(li,n):
    result=[]
    for i in range(1,n+1):
     if str(i) not in li:
        result.append(i)
    return result
li=input().split()
n=max(map(int,li))
print(mis_Element(li,n))



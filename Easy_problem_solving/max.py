def maximum(li,maxi):
    for i in li:
      if maxi<int(i):
        maxi=int(i)
    return maxi
li=input().split()
maxi=int(li[0])
print(maximum(li,maxi))

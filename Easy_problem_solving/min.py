def minimum(li,mini):
    for i in li:
     if mini>i:
        mini=int(i)
    return mini
li=input().split()
mini=li[0]
print(minimum(li,mini))

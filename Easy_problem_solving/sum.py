def addi(li):
 add=0
 for i in li:
    add+=int(i)
 return add
li=input().split()
print(addi(li))

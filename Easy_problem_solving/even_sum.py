'''li=input().split()
add=0
for i in li:
    if int(i)%2==0:
        add+=int(i)
print(add)'''
#using function
def even_sum(li):
    even_add=0
    for i in li:
        if int(i)%2==0:
            even_add+=int(i)
    return even_add
li=input().split()
print(even_sum(li))

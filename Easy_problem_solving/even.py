'''li=input().split()
even=list()
for i in li:
    if int(i)%2==0:
        even.append(int(i))
print(even)'''
#using function
def evens(li):
    even=list()
    for i in li:
        if int(i)%2==0:
          even.append(int(i))
    return even
li=input().split()
print(evens(li))


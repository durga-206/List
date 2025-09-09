def numbers_moving(li):
    new1,new2=[],[]
    for i in li:
        if i<0:
            new1.append(i)
        else:
            new2.append(i)
    return new1+new2
li=input().split()
li1=list(map(int,li))
print(numbers_moving(li1))

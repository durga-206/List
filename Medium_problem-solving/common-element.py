def common(li1,li2):
    com=[]
    for i in range(len(li1)):
        for j in range(len(li2)):
            if li1[i]==li2[j]:
                com.append(li1[i])
    return com
li1=input().split()
li2=input().split()
print(common(li1,li2))


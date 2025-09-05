li=[2,3,5,4,7]
for i in range(len(li)-1):
    for j in range(i+1,len(li)-1):
        if int(li[i])+int(li[j])==7:
            print(f"({li[i]},{li[j]})", end='')


def pair_add(li,target):
 for i in range(len(li)-1):
    for j in range(i+1,len(li)-1):
        if int(li[i])+int(li[j])==target:
            print(f"({li[i]},{li[j]})", end='')
li=input().split()
target=int(input())
pair_add(li,target)

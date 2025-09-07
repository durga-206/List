def reverse(lis):
 reverse_li=[]
 for i in range(len(lis)-1,-1,-1):
    reverse_li.append(int(lis[i]))
 return reverse_li
lis=input().split()
print(reverse(lis))

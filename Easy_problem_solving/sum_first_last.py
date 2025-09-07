def sum_first_last(li):
 first=li[0]
 last=li[len(li)-1]
 return int(first)+int(last)
li=input().split()
print(sum_first_last(li))

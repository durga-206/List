def product(li,prod):
 for i in li:
    prod*=int(i)
 return prod
li=input().split()
prod=1
print(product(li,prod))

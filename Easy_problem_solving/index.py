def index(li,target):
 for i in range(0,len(li)-1):
      if target==int(li[i]):
         return i
li=input().split()
target=int(input('Enter the Target element: '))
print(index(li,target))

      

def square(li):
 square=list()
 for i in li:
    square.append(int(i)*int(i))
 return square
li=input().split()
print(square(li))
    

#over
list=[]
a=int(input("enter the no of numbers:"))
for i in range(a):
  x=int(input("Enter the number:"))
  if x<=100:
    list.append(x)
  else:
    list.append("over")
print(list)
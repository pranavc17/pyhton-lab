#list intersection
list1=["red","blue","green","yellow"]
list2=["blue","green","orange",]
print("list1",list1)
print("list2",list2)
print([i for i in list1 if i not in list2])

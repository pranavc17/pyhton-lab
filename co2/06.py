# number of characters
st = input("enter the string:")
c = 0
for i in range(0, len(st)):
    if st[i].isalpha():
        c = c + 1
print("count=", c)
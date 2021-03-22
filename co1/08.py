#replace with dollar
word=input("Enter the word:")
l=len(word)
a=word[0]
for x in word[1:l]:
    if x==a:
        word=word.replace(a,'$')
print(a+word[1:l])

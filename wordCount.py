word=input()
count=0
for i in word:
    if i.islower():
        count+=1
print(word.upper())
print(count)

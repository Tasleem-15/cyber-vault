x=input("Enter the sentence which u want : ")
freq={}
words=x.split()
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(len(words))
print(freq)

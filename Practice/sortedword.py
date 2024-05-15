word=input("Word:")
letterdictionary={}
sortedword=sorted(word)
setword=set(word)
uniqlist=sorted(list(setword))
for letter in uniqlist:
    lettercount=sortedword.count(letter)
    letterdictionary[letter]=lettercount
print(letterdictionary)
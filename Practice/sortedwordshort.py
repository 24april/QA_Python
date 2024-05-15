word=input("Word:")
letterdictionary={}
uniqlist=sorted(list(set(word)))
for letter in uniqlist:
    letterdictionary[letter]=word.count(letter)
print(letterdictionary)
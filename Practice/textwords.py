import re
text = """""
There are many variants of Lorem Ipsum, but most of them do not always have acceptable modifications, for example, humorous inserts or words that do not even remotely resemble Latin. If you need Lorem Ipsum for a serious project, you probably don't want some joke hidden in the middle of a paragraph. Also, all other well-known Lorem Ipsum generators use the same text, which they simply repeat until they reach the desired volume.
"""""
uniqwords=[]
wordscount=[]
textwithoutpunct=re.sub(r'[^\w\s]', '', text)
textwithoutpunct=textwithoutpunct.lower()
words=textwithoutpunct.split()
wordsset=set(words)
for word in wordsset:
    if word in uniqwords:
        index=uniqwords.index(word)
        wordscount[index]+=1
    else:
        uniqwords.append(word)
        wordscount.append(1)
maxcount=max(wordscount)
mostword=uniqwords[wordscount.index(maxcount)]
print("Самое часто встреч. слово",mostword,maxcount)
import re
text = """""
There are many variants of Lorem Ipsum, but most of them do not always have acceptable modifications, for example, humorous inserts or words that do not even remotely resemble Latin. If you need Lorem Ipsum for a serious project, you probably don't want some joke hidden in the middle of a paragraph. Also, all other well-known Lorem Ipsum generators use the same text, which they simply repeat until they reach the desired volume.
"""""
countedamounts=[]
countedwords=[]
textwithoutpunct=re.sub(r'[^\w\s]','', text)
textwithoutpunct=textwithoutpunct.lower()
wordslist=textwithoutpunct.split()
wordsset=set(wordslist)
uniqlist=list(wordsset)
for word in uniqlist:
    countamount=wordslist.count(word)
    countedamounts.append(countamount)
    countedwords.append(word)
mostamount=max(countedamounts)
print("Самое часто встреч. слово:",countedwords[countedamounts.index(mostamount)],". Kол-во в тексте:",mostamount)
input()

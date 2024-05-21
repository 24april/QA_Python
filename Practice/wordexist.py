import re
str="""""
There are many variants of Lorem Ipsum, but most of them do not always have acceptable modifications, for example, humorous inserts or words that do not even remotely resemble Latin. If you need Lorem Ipsum for a serious project, you probably don't want some joke hidden in the middle of a paragraph. Also, all other well-known Lorem Ipsum generators use the same text, which they simply repeat until they reach the desired volume.
"""""
def searchword(word,str):
    strwithoutpunct=re.sub(r'[^\w\s]','',str)
    strwithoutpunct=strwithoutpunct.lower()
    wordslist=strwithoutpunct.split()
    if wordslist.count(word)==0:
        print("Word",word,"does not exist in str.")
    else:
        print("Word",word,"exists in str.(",wordslist.count(word),")")
    return word
print(searchword("the",str))
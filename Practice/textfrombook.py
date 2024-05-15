import re
searchword=input("Word:")
searchword=searchword.lower()
with open('textfrombook.txt',encoding='utf8') as filetext:
    textvar=filetext.read()
    print(textvar)
    textwithoutpunct=re.sub(r'[^\w\s]','', textvar)
    textwithoutpunct=textwithoutpunct.lower()
    wordslist=textwithoutpunct.split()
    print(wordslist)
    print(f"Word {searchword} found in text: {wordslist.count(searchword)}")
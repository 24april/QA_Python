def count_letters(word):
    word=word.lower()
    letterdictionary={}
    uniqlist=sorted(list(set(word)))
    for letter in uniqlist:
        if letter.isalpha():
            letterdictionary[letter]=word.count(letter)
    return letterdictionary
word=input("Word:")
letterdictionary=count_letters(word)
print(letterdictionary)
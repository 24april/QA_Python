import random
def randomphrasefromfile(filename):
    try:
        with open(filename,"r",encoding="utf8") as filephrases:
            return random.choice(filephrases.readlines())
    except FileNotFoundError:
        return "File not found"
print(randomphrasefromfile('textfrombook.txt'))
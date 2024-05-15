try:
    with open('textfrombook.txt','r',encoding="utf8") as filetext:
        print(filetext.read())
except FileNotFoundError:
    print("File Not Found")
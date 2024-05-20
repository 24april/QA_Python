user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}
import re
def check_emails(mail):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern,mail):
        return False
    parts = mail.split('@')
    if len(parts[0])<5:
        return False
    return True
def checkpassword(password):
    return len(password)>=8 and (password.islower()==False) and (password.isupper()==False) and any(i.isdigit() for i in password) and (any(i.isalnum()==False for i in password) and any(i.isalpha() for i in password))
def checkname(name):
    name=name.replace("-","")
    name=name.replace(" ", "")
    if len(name)<2:
        return False
    return name.isalpha()
def registration():
    while True:
        name=input("Name:")
        mail=input("E.mail address:")
        password=input("Password:")
        if checkname(name) and checkpassword(password) and check_emails(mail) and (mail not in user_database.keys()):
            print("Registration was succesful.")
            user_database[mail]={'name':name,'password':password}
        else:
            if checkname(name)==False:
                print("Incorrect name.")
            if check_emails(mail)==False:
                print("Invalid address.")
            if checkpassword(password)==False:
                print("Invalid password.")
            if mail in user_database.keys():
                print("Address was already used.")
        y=input("Show user database(y)?")
        if y=="y":
            print(user_database)
            break
registration()
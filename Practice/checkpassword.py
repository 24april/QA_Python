def checkpassword(password):
    return len(password)>=8 and (password.islower()==False) and (password.isupper()==False) and any(i.isdigit() for i in password) and (any(i.isalnum()==False for i in password) and any(i.isalpha() for i in password))
pwd=input("Password:")
print(checkpassword(pwd))
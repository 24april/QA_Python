def checkpassword(password):
    return len(password)>=8 and any(i.isdigit() for i in password) and any(i.isalpha() for i in password) and (password.startswith("+") or password.endswith("+"))
pwd=input("Password:")
print(checkpassword(pwd))
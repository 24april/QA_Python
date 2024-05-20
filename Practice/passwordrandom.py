import random
def randompassword(lenghth):
    password=""
    while ((password.islower()==False) and (password.isupper()==False) and any(i.isdigit() for i in password) and (any(i.isalnum()==False for i in password)) and any(i.isalpha() for i in password))==False:
        password=""
        for _ in range(lenghth):
            password+=random.choice(r"""#$%&'()*+,-./:\;<=>?@[]^_`{|}~1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"!""")
    return password
print(randompassword(4))
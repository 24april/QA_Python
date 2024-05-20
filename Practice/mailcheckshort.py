import re


def check_emails(mail):
    #создаю паттерн для проверки формата адреса email
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


    if not re.match(pattern,mail):
        return False
   
    parts = mail.split('@')


    if len(parts[0])<4:
        return False
   
    return True


   
print(check_emails('example@email.com')) # True
print(check_emails('invalid.email@domain'))  #False
print(check_emails('another.example@sub.domain.com'))  #True
print(check_emails('invalid_enother?@domain.name')) # false
print(check_emails('we@domain.name')) # false

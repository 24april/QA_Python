def validphone(phone):
    if phone[0]!="+":
        return False
    phone=phone.replace("+","")
    if len(phone)!=11:
        return False
    if phone.isdigit():
        return True
    return False
phone=input("Phone: ")
print(validphone(phone))
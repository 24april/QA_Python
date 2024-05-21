phonebook={"Name1":"+12345678901"}
def validphone(phone):
    if phone[0]!="+":
        return False
    phone=phone.replace("+","")
    if len(phone)!=11:
        return False
    if phone.isdigit():
        return True
    return False
def inputphone(inputtext="Phone:"):
    phone=input(inputtext)
    while validphone(phone)==False:
        print("Invalid input.")
        phone=input(inputtext)
    return phone
def writephonebook(phonebook):
    while True:
        name=input("Name:")
        phone=inputphone()
        phonebook[name]=phone
        y=input("Show phonebook(y)?")
        if y.lower()=="y":
            print(phonebook)
            break
writephonebook(phonebook)
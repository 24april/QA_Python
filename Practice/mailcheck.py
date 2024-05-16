def mailcheck(address):
    address=address.lower()
    if address.count("@")!=1:
        return 'Address must contain 1 "@".'
    addresssplit=address.split("@")
    if len(addresssplit[0])<6:
        return 'Login must contain 6 symbols.'
    for i in addresssplit[0]:
        if i not in "qwertyuiopasdfghjklzxcvbnm1234567890-_.":
            return 'Login must contain only latin letters,digits and "-","_","."'
    domain=addresssplit[1]
    if domain.count(".")==0:
        return "Invalid domain."
    for i in domain:
        if i not in "qwertyuiopasdfghjklzxcvbnm1234567890-.":
            return 'Domain must contain only latin letters,digits and "-","."'
    domainsplit=domain.split('.')
    if len(domainsplit[len(domainsplit)-1])<2:
        return "Invalid domain"
    for i in domainsplit[len(domainsplit)-1]:
        if i not in 'qwertyuiopasdfghjklzxcvbnm':
            return 'Incorrect domain'
    return "Valid address."
address=input("Address @:")
print(mailcheck(address))
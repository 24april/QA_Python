def validate_str(str):
    if "@" not in str:
        return False
    if "." not in str:
        return False
    str=str.split("@")
    if "." not in str[1]:
        return False
    return True
print(validate_str("e.rik@mailru")) 
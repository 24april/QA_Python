def validate_text_length(text,maxlength):
    if len(text)>maxlength:
        return False
    return True
print(validate_text_length("Aa",5))
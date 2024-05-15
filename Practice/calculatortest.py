def calctest(operator,a,b):
    try:
        if operator=="+":
            return a+b
        elif operator=="-":
            return a-b
        elif operator=="/":
            return a/b
        elif operator=="*":
            return a*b
        else:
            return "Incorrect operator type."
    except ZeroDivisionError:
        return "Division by zero."
    except TypeError:
        return "Incorrect number type."
print(calctest("/","m",0))
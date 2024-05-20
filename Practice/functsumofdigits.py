def sumofdigits(number):
    try:
        return sum([int(i) for i in number])
    except ValueError:
        return "Value is not integer number"
number=input("Integer number:")
print(sumofdigits(number))
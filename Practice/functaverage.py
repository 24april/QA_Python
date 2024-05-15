def average(list):
    try:
        return sum(list)/len(list)
    except TypeError:
        return "Incorrect data type."
    except ZeroDivisionError:
        return 0
nlist=[6,7,9,6,10]
print(average(nlist))
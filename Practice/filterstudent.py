studentslist=[{'name':'Student1','grades':[]},{'name':'Student2','grades':[5,3,4,2]},{'name':'Student3','grades':[5]}]
def average(list):
    try:
        return sum(list)/len(list)
    except TypeError:
        return "Incorrect data type."
    except ZeroDivisionError:
        return 0
def filter_students(studentslist):
    studentsfiltered=[]
    for student in studentslist:
        if average(student['grades'])>=4:
            studentsfiltered.append(student['name'])
    return studentsfiltered
print(filter_students(studentslist))
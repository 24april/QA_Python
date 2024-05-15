test_scores = [75,90,85,60,95]
prog_scores = [80,70,90,85,75]
student=0
print(test_scores,prog_scores)
for test_scores,prog_scores in zip(test_scores,prog_scores):
    print(test_scores,prog_scores)
    student+=1
    if test_scores>80 and prog_scores>80:
        print(f"Cтудент №{student} с оценками выше 80:",test_scores,prog_scores)
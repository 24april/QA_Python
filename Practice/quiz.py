import random
questions={"Question1?":["A","B","C","D","C"],"Question2?":["A","B","C","D","A"],"Question3?":["A","B","C","D","D"]}
def quiz(questions):
    questionslist=list(questions.keys())
    scores=0
    random.shuffle(questionslist)
    for question in questionslist:
        print(question)
        print("Var of answers:",questions[question][:len(questions[question])-1])
        answer=input("Answer:")
        while answer not in questions[question]:
            print("Incorrect var.")
            answer=input("Answer:")
        if answer==questions[question][len(questions[question])-1]:
            scores+=1
    print(f"Correct answers: {scores} of {len(questions)}.")
quiz(questions)
import random
joke_template = [
    'Почему {} катится вниз?',
    'Потому что {} смеятся над ним!',
    'Кто {} в книгах?',
    'Кто {}?',
    'Что сказал {} ему {} когда они встретились ?'
]
joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка'
]
random_joke_template=random.choice(joke_template)
print(random_joke_template.format(*random.sample(joke_elements,random_joke_template.count('{}'))))
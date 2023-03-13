import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4

def poser_question():
    a, b = random.randint(NOMBRE_MIN, NOMBRE_MAX), random.randint(NOMBRE_MIN, NOMBRE_MAX)
    result = a + b
    response = input(f'Calculez: {a} + {b} = ')
    reponse_int = int(response)

    if reponse_int == result:
        return True

    return False

nb_points = 0
for i in range(1, NB_QUESTIONS+1):
    print(f'question {i}/{NB_QUESTIONS}')
    if poser_question():
        print('reponse correcte')
        nb_points +=1
    else:
        print('reponse incorrecte')
    print()

print(f'votre note est: {nb_points}/{NB_QUESTIONS}')

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print('Excellent!')
elif nb_points > moyenne and != NB_QUESTIONS:
    print('pas mal')
elif nb_points < moyenne and != 0:
    print('peut mieux faire')
elif nb_points == 0:
    print('Révisez vos math!')



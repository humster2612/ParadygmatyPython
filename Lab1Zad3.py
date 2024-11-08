# zad3

taski = [
    {'Czas wykonania': 2, 'nagroda': 11},
    {'Czas wykonania': 5, 'nagroda': 8},
    {'Czas wykonania': 3, 'nagroda': 4},
    {'Czas wykonania': 4, 'nagroda': 9},
]


def Proceduralnie(taski):

    taski.sort(key=lambda x: x['Czas wykonania'])

    czas_oczekiwania = 0
    aktualny_czas = 0

    kolejnosc = []

    for task in taski:

        kolejnosc.append(task)
        czas_oczekiwania += aktualny_czas
        aktualny_czas += task['Czas wykonania']

    return kolejnosc, czas_oczekiwania


kolejnosc, czas_oczekiwania = Proceduralnie(taski)




print("Kolejność zadań:", kolejnosc)
print("Czas oczekiwania:", czas_oczekiwania)

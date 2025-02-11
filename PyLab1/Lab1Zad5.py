# Zad 5

taski = [
    (2, 6, 7),
    (1, 4, 10),
    (4, 8, 5),
    (5, 9, 12),
    (3, 7, 3),
    (6, 10, 6),
    (0, 5, 8)
]

def procedur(taski):

    taski.sort(key=lambda x: x[1])


    wybrane_taski = []
    maksymalna_nagroda = 0
    zakonczenie = 0

    for task in taski:

        poczatek, koniec, nagroda = task
        if poczatek >= zakonczenie:

            wybrane_taski.append(task)
            maksymalna_nagroda += nagroda
            zakonczenie = koniec

    return maksymalna_nagroda, wybrane_taski

maksymalna_nagroda, wybrane_taski = procedur(taski)
print("Maksymalna Nagroda:", maksymalna_nagroda)
print("Wybrane taski:", wybrane_taski)
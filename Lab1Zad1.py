# zad1

def podzialPaczek(wagi, max_waga):
    for waga in wagi:

        if waga > max_waga:
            raise ValueError(f"Waga paczki {waga} przekracza dozwolone maksymalne wage kursu {max_waga}")
    sort_wagi = sorted(wagi, reverse = True)
    kursy = []

    for waga in sort_wagi:
        added = False

        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                added = True
                break

        if not added:
            kursy.append([waga])
    return len(kursy), kursy


wagi = [21,5,8,15,10,10,7]

max_wag = 25

licz_kurs, kursy = podzialPaczek(wagi, max_wag)

for i, kurs in enumerate(kursy, 1):
    print(f" Kurs {i} : {kurs} -> suma wagi : {sum(kurs)} kg")
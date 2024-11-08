# zad4

def plecak(wagi, wartosci, pojemnosc):

    przedmioty = len(wagi)

    arrpojemnosc = [0] * (pojemnosc + 1)


    for item in range(przedmioty):

        for j in range(pojemnosc, wagi[item] - 1, -1):
            arrpojemnosc[j] = max(arrpojemnosc[j], arrpojemnosc[j - wagi[item]] + wartosci[item])


    wybrane_przedmioty = []
    item = pojemnosc
    for j in range(przedmioty - 1, -1, -1):

        if item - wagi[j] >= 0 and arrpojemnosc[item] != arrpojemnosc[item - wagi[j]]:
            wybrane_przedmioty.append(j)
            item -= wagi[j]

    wybrane_przedmioty.reverse()

    return arrpojemnosc[pojemnosc], wybrane_przedmioty



wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 6]
pojemnosc = 5

maksymalna_wartosc, wybrane_przedmioty = plecak(wagi, wartosci, pojemnosc)



print(f'Maksymalna wartość: {maksymalna_wartosc}')

print(f'Wybrane przedmioty: {wybrane_przedmioty}')

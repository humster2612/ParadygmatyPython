def analiza_danych(data):


    liczby = list(filter(lambda x: isinstance(x, (int, float)), data))

    licz_maks = max(liczby) if liczby else None




    napis = list(filter(lambda x: isinstance(x, str), data))
    dluzszy_napis = max(napis, key=len) if napis else None

    return {

        "maksymalna_liczba": licz_maks,
        "najdłuższy_napis": dluzszy_napis
    }



data = [
    57, "apple", 127.89, "banana", "grape", "peach", 100, "tree"
]

result = analiza_danych(data)

print("Największa liczba:", result["maksymalna_liczba"])
print("Najdłuższy napis:", result["najdłuższy_napis"])

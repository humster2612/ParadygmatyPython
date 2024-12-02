class Pracownik:

    def __init__(self, imie, wiek, wynagrodzenie):


        self.imie = imie
        self.wiek = wiek
        self.wynagrodzenie = wynagrodzenie

    def __str__(self):

        return f"Imię: {self.imie}, Wiek: {self.wiek}, Wynagrodzenie: {self.wynagrodzenie} "





class MenedzerPracownikow:

    def __init__(self):
        self.lista_pracownikow = []

    # Dodawanie pracownik

    def dodaj_pracownika(self, pracownik):

        self.lista_pracownikow.append(pracownik)

    # wyswietlan pracownik

    def wyswietl_pracownikow(self):
        if not self.lista_pracownikow:

            print("Brak pracowników.")

        else:
            for pracownik in self.lista_pracownikow:

                print(pracownik)

    #usuwanie

    def usun_pracownikow_w_wieku(self, minimalny_wiek, maksymalny_wiek):

        self.lista_pracownikow = [
            pracownik for pracownik in self.lista_pracownikow
            if not (minimalny_wiek <= pracownik.wiek <= maksymalny_wiek)

        ]



    def znajdz_pracownika(self, imie):

        for pracownik in self.lista_pracownikow:
            if pracownik.imie == imie:
                return pracownik


        return None


    def aktualizuj_wynagrodzenie(self, imie, nowe_wynagrodzenie):


        pracownik = self.znajdz_pracownika(imie)

        if pracownik:

            pracownik.wynagrodzenie = nowe_wynagrodzenie
            print(f"Wynagrodzenie  {imie} zostalo zaktualizowane.")
        else:
            print(f"Pracownik o imieniu {imie} nie zostal znaleziony.")





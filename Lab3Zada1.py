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


class MenedzerFrontend:
    def __init__(self):
        self.menedzer_pracownikow = MenedzerPracownikow()

    def menu(self):
        while True:
            print("\n-------------------------------------- System Pracowników --------------------------------------")
            print("1. Dodaj nowego pracownika do listy ")
            print("2. Pokaż pracowników z listy ")
            print("3. Usuń pracowników w przedziale wiekowym ")
            print("4. Aktualizuj  wynagrodzenia pracownika według jego imienia i nazwiska ")
            print("5. Zakończ")

            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                imie = input("Podaj imię i nazwisko pracownika: ")
                wiek = int(input("Podaj wiek pracownika: "))
                wynagrodzenie = float(input("Podaj wynagrodzenie: "))
                pracownik = Pracownik(imie, wiek, wynagrodzenie)
                self.menedzer_pracownikow.dodaj_pracownika(pracownik)
                print("Pracownik został dodany.")
            elif wybor == "2":
                self.menedzer_pracownikow.wyswietl_pracownikow()
            elif wybor == "3":
                minimalny_wiek = int(input("Podaj minimalny wiek: "))
                maksymalny_wiek = int(input("Podaj maksymalny wiek: "))
                self.menedzer_pracownikow.usun_pracownikow_w_wieku(minimalny_wiek, maksymalny_wiek)
                print("Pracownicy zostali usunięci.")
            elif wybor == "4":
                imie = input("Podaj imię i nazwisko pracownika: ")
                nowe_wynagrodzenie = float(input("Podaj nowe wynagrodzenie: "))
                self.menedzer_pracownikow.aktualizuj_wynagrodzenie(imie, nowe_wynagrodzenie)
            elif wybor == "5":

                break
            else:
                print(" Wybrałeś żłe. Spróbuj jeszcze raz.")



if __name__ == "__main__":
    frontend = MenedzerFrontend()
    frontend.menu()



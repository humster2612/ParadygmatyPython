from functools import reduce
import numpy as np


def operacje_macierzowe(macierz1, macierz2, operacja):
    if operacja=='suma':

        return np.add(macierz1, macierz2)

    elif operacja== 'iloczyn':
        return np.dot(macierz1, macierz2)



def poloczenie(macierze, operacja):
    return reduce(lambda m1, m2: operacje_macierzowe(m1, m2, operacja), macierze)


macierz1=np.array([[22, 34], [3, 4]])
macierz2=np.array([[5, 53], [12, 21]])
macierz3=np.array([[7, 11], [8, 25]])


macierze= [macierz1, macierz2, macierz3]


operacja =input("Jaką chcęsz operację, wybierz suma / iloczyn: ").strip().lower()


if operacja=='suma' or operacja =='iloczyn':

    wynik = poloczenie(macierze, operacja)

    print(f"Wynik operacji '{operacja}' na macierzach:\n{wynik}")
else:
    print("Błąd!")

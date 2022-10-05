from PIL import Image
import numpy as np

#Zad 2

obrazek = Image.open("lab1/inicjaly.bmp")
obrazek.show()
print("informacje o obrazie ")
print("tryb", obrazek.mode)
print("format", obrazek.format)
print("rozmiar", obrazek.size)

#Zad 3

tablica_bool = np.asarray(obrazek)
tablica_int = tablica_bool * 1
print(tablica_int)

text = open('lab1/inicjaly.txt', 'w')
for rows in tablica_int:
    for item in rows:
        text.write(str(item) + ' ')
    text.write('\n')

#Zad 4

dane_obrazka = np.asarray(obrazek)
print("---------------- informqcje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy:", dane_obrazka.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("liczba elementow:", dane_obrazka.size)  # liczba elementów tablicy
print("wymiar tablicy:", dane_obrazka.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)  # pokazuje ile współrzednych trzeba do opisania wyrazu tablicy (piksela)
print("50,30:", dane_obrazka[30][50])
print("90,40:", dane_obrazka[40][90])
print("99,0:", dane_obrazka[0][99])
print("***************************************")
print(dane_obrazka)  # mozna odkomentować, zeby zobaczyć tablicę

dane_obrazka1 = np.asarray('lab1/inicjaly.txt')
print("---------------- informqcje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka1.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy:", dane_obrazka1.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("liczba elementow:", dane_obrazka1.size)  # liczba elementów tablicy
print("wymiar tablicy:", dane_obrazka1.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:",
      dane_obrazka1.itemsize)  # pokazuje ile współrzednych trzeba do opisania wyrazu tablicy (piksela)
print("50,30:", dane_obrazka1[30][50])
print("90,40:", dane_obrazka1[40][90])
print("99,0:", dane_obrazka1[0][99])
print("***************************************")
print(dane_obrazka1) # mozna odkomentować, zeby zobaczyć tablicę
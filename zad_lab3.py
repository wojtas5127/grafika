import random

from PIL import Image
import numpy as np


def negatyw(tab, n):
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i][j] = 255 - tab[i][j]
    ramka = Image.fromarray(tab_neg)
    ramka.save("lab3/zad3_obraz" + str(n) + "N.bmp")
    ramka.show()
    return tab_neg


def zad3_1_przerobione(w, h, dzielnik, kolor_ramki, kolor):
    t = (h, w)
    kolory = [kolor_ramki, kolor]
    tab = np.zeros(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    i = 0
    while z1 >= grub and z2 >= grub:
        tab[(i+1)*grub:z1, (i+1)*grub:z2] = kolory[(i+1) % 2]-10*i
        z1 -= grub
        z2 -= grub
        i += 1
    tab = tab * 255
    ramka = Image.fromarray(tab)
    ramka.save("lab3/zad3_obraz1.bmp")
    ramka.show()
    return tab


t1 = zad3_1_przerobione(100, 50, 10, 200, 50)
negatyw(t1, 1)


def zad3_4_przerobione(w, h, dzielnik_w, dzielnik_h, kolor_ramki, kolor):
    t = (h, w)
    kolory = [kolor_ramki, kolor]
    tab = np.ones(t, dtype=np.uint8)
    grub_w = int(w/dzielnik_w)
    grub_h = int(h/dzielnik_h)
    for k1 in range(dzielnik_h):
        for g1 in range(grub_h):
            i = g1 + k1 * grub_h
            i1 = 1
            for k2 in range(dzielnik_w):
                for g2 in range(grub_w):
                    j = g2 + k2 * grub_w
                    j1 = 1
                    tab[i, j] = kolory[((k1 % 2) + (k2 % 2)) % 2]-i1-j1
    tab = tab * 255
    ramka = Image.fromarray(tab)
    ramka.save("lab3/zad3_obraz4.bmp")
    ramka.show()
    return tab


t4 = zad3_4_przerobione(100, 50, 10, 8, 200, 150)
negatyw(t4, 4)


def zad3_2_przerobione(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w/dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            j = g + k * grub
            for i in range(h):
                tab[i, j] = k % 2
    tab = tab * 255
    ramka = Image.fromarray(tab)
    ramka.save("lab3/zad3_obraz2.bmp")
    ramka.show()
    return tab

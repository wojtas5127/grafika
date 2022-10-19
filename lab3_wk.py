from PIL import Image
import numpy as np

def negatyw(tab, n):
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i][j] = 255 - tab[i][j]
    ramka = Image.fromarray(tab_neg)
    ramka.save("lab1/obraz3_1N.jpg")
    ramka.save("lab1/obraz3_1N.png")
    ramka.show()
    return tab_neg


def zad3_1(w, h, dzielnik, kolor_ramki, kolor):
    t = (h, w)
    kolory = [kolor_ramki, kolor]
    tab = np.zeros(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    i = 0
    while z1 >= grub and z2 >= grub:
        tab[(i+1)*grub:z1, (i+1)*grub:z2] = kolory[(i+1) % 2]-5*i
        z1 -= grub
        z2 -= grub
        i += 1
    tab = tab * 255
    ramka = Image.fromarray(tab)
    ramka.save("lab1/obraz3_1.jpg")
    ramka.save("lab1/obraz3_1.png")
    ramka.show()
    return tab


t1 = zad3_1(100, 50, 10, 200, 50)
negatyw(t1, 1)
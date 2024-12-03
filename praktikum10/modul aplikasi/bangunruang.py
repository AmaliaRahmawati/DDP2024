import math

def luas_kubus(sisi):
    hasil = 6 * sisi ** 2
    print(f'luas kubus adalah 6 * {sisi} ** 2 = {hasil}')

def luas_balok(panjang, lebar, tinggi):
    hasil = 2 * (panjang*lebar +  panjang*tinggi + lebar*tinggi)
    print(f'luas balok adalah 2 * {panjang}*{lebar} + {panjang}*{tinggi} + {lebar}*{tinggi} = {hasil}')

def luas_tabung(jari, tinggi):
    hasil = 2 * 22/7 * jari * (jari + tinggi)
    print(f'luas tabung adalah 2 * 22/7 * {jari} * {jari}+{tinggi} = {hasil}')

def luas_limas(alas, tinggi, sisi):
    hasil = (4 * 1/2 * alas * tinggi) + (sisi * sisi)
    print(f'luas limas adalah {(4 * 1/2 * alas * tinggi)} + {(sisi * sisi)} = {hasil}')

def luas_prisma_segitiga(alas, t, tinggi, c):
    hasil = 2 * (1/2 * alas * t) + (alas + t + c) * tinggi
    print(f'luas prisma adalah 2 * {(1/2 * alas * t)} + {(alas + t + c)} * {tinggi} = {hasil}')

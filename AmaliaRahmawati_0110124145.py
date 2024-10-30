#masukan list [namakendaraan],[jenis kendaraan], [cckendaraan], [warna kendaraan], [roda kendaraan]
kendaraanku = ['Honda Beat', 'Sepeda Motor', 125, 'Pink', 2]
print("kendaraan saya adalah:", kendaraanku)
print("==================")
#tambahkan dari list tsb di belakang dgn value: [harga kendaraan, tipe kendaraan]
kendaraanku.append(50000000)
print(kendaraanku)
kendaraanku.append('matic')
print(kendaraanku)

#kendaraanku.extend(50000000, matic) cara cepat
print('=============')

#tambahkan setelah jenis kendaraan dgn value [merk kendaraan]
kendaraanku.insert(2,'Beat')
print(kendaraanku)
print('=============')


# membuat match case untuk mengitung bangun datar. jika pilih1 maka menghitung luas persegi, pilih2 maka menghitung luas lingkaran, pilih3 maka menghitung luas segitiga
print('ini adalah program sederhana untuk menghitung luas bangun datar')
print('pilih menu angka 1-3:\n1. Persegi\n2. Lingkaran\n3. Segitiga')
pilihMenu = int(input('masukan pilihan 1-3: '))
match pilihMenu:
    case 1:
        print('kamu telah memilih persegi')
        sisi = int(input('masukan nilai yg mau dihitung: '))
        hitung = sisi * sisi
        print(f'Luas persegi adalah : {hitung}')
    case 2: 
        print('Kamu telah memilih lingkaran ')
        r = int(input('masukan nilai yg mau dihitung: '))
        hitung = 3,14 * r * r
        print(f'Luas Lingkaran adalah: {hitung}')
    case 3:
        print('Kamu telah memilih segitiga')
        alas = int(input('masukan nilai alas: '))
        tinggi = int(input('masukan nilai tinggi: '))
        hitung= 1/2 * alas * tinggi
        print(f'Luas Segitiga adalah: {hitung}')
    case _: 
         print('masukan pilihan yang benar')
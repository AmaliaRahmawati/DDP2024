print('## nomor 1 ##')
#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
def celcius_ke_fahrenheit(celcius):
  fahrenheit= (9/5*celcius)+32
  return fahrenheit

#cetak 0 celcius ke 32 fahrenheit
suhu_celcius1 = 0
suhu_fahrenheit1 = celcius_ke_fahrenheit (suhu_celcius1)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)

#cetak 100 celcius ke 212 fahrenheit
suhu_celcius2 = 100
suhu_fahrenheit2 = celcius_ke_fahrenheit (suhu_celcius2)
print('suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)



print()
print('## nomor 2 ##')
def genap_ganjil(bilangan):
  hitung = bilangan%2==0 #menentukan bilangan ganjil atau bilangan genap
  return hitung #mengembalikan nilai hitung

angka = 4
hasil = genap_ganjil(angka)
print(f"bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"bilangan {angka2} bernilai {hasil2}")



print()
print('## nomor 3 ##')
def lulus_tidaklulus(nilai):
  if nilai >60:
    return 'lulus'
  else:
    return 'gagal'
  
nilai_kamu = 80
ket = lulus_tidaklulus(nilai_kamu)
print(f"nilai: {nilai_kamu}, keterangan: {ket}")

nilai_kamu = 60
ket = lulus_tidaklulus(nilai_kamu)
print(f"nilai: {nilai_kamu}, keterangan: {ket}")



print()
print('## nomor 4 ##')
def bilangan(x):
    for i in range(1, x, 2):
        print(i, end=', ' if i < x - 2 else '\n')

# Pemanggilan fungsi
bilangan(20)









angka1 = int(input('Masukkan Angka Pertama :'))
angka2 = int(input('Masukkan Angka Kedua :'))
print('Operator: 1. penjumlahan \n2. pengurangan \n'
     '3. Perkalian \n4. Pembagian')
pilih=int(input('Pilih Operator : '))
if pilih == 1:
    tambah = angka1+angka2
    print('Hasilnya Adalah ',tambah)
elif pilih == 2:
    kurang = angka1-angka2
    print('Hasilnya Adalah ',kurang)
elif pilih == 3:
    kali = angka1*angka2
    print('Hasilnya Adalah ',kali)
elif pilih == 4:
    kurang = angka1/angka2
    print('Hasilnya Adalah ',bagi)
else:
    print('Operator yang anda masukkan tidak ada')
    
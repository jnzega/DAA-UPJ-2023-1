import datetime as dt

dt_now = dt.datetime.now()

nim = 2022071065

Mahasiswa = ["Joshua Nathanael Zega", str(nim), "Informatika", "Desain Analisis dan Algoritma", dt_now.strftime('%d %m %Y, %H:%M:%S'), "Universitas Pembangunan Jaya"]

print(Mahasiswa[2:3])

bin_colors=["Red", "Green", "Blue", "Yellow"]

print(bin_colors[1:4])

for warnaNich in bin_colors:
    print((warnaNich + " Square"))

for kampus in Mahasiswa:
    print(("UPJ " + kampus))

bin_warna = ('Red', 'Green', 'Blue', 'Yellow')
print(bin_warna)

UPJ = ("Universitas", "Pembangunan", "Jaya")

pertama = (100)
kedua = (200, 400, 600)
ketiga = (300)
keempat = (400, 800)

nested_tuple = (pertama, kedua, ketiga, keempat)

print(nested_tuple)
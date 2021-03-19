#Membuat list teman
list_teman = ['Retno', 'Ica', 'Yuki', 'Sekar', 'Stefany', 'Raysa', 'Rana', 'Salma', 'Diva', 'Putri']

#Menampilkan isi list indeks nomor 4,6,7
print("Nama teman 4,6,7 : ", list_teman[4], ",", list_teman[6], ",", list_teman[7])

#Mengganti nama teman pada list 3,5,9
list_teman[3] = 'Talitha'
list_teman[5] = 'Rara'
list_teman[9] = 'Alvin'

#Menambah nama teman
list_teman.extend(['Cita', 'Rafli'])

#Menampilkan list nama teman dengan perulangan
urutan = 0
for data in range(0, 12):
    print(list_teman[urutan])
    urutan = urutan + 1

#Menampilkan panjang list
print(len(list_teman))
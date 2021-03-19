#Dictionary berisi hobi, sosial media, lagu kesukaan, makanan favorit
dict = {'Nama' : ['Sylvia Cahyaningtyas'],
        'Hobi' : ['Menonton film', 'Mendengarkan musik', 'Bersepeda'],
        'Sosial media' : ['Instagram : @sylviactyas', 'Twitter : sylviactyas', 'Line : sylviactyas'],
        'Lagu kesukaan' : ['To my youth', 'Angel', 'Fight song'],
        'Makanan favorit' : ['Nasi goreng', 'Seblak', 'Mie']}
print(dict)

#Mengubah salah satu hobi dan sosial media
dict['Hobi'][2] = ('Membaca')
dict['Sosial media'][2] = ('Facebook : Sylvia Cahyaningtyas')

#Menghapus 2 makanan favorit
del dict['Makanan favorit'][0:2]

#Menambahkan satu hobi
dict['Hobi'].append('Bermain game')

print(dict)
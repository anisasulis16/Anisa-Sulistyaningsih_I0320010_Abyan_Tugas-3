#Pemograman dengan kaidah dictionary

identitas_diri = {'Nama':'Anisa Sulistyaningsih',
                  'Hobi1':'Membaca Novel',
                  'Hobi2':'Menyanyi',
                  'Hobi3':'Menari',
                  'Hobi4':'Memasak',
                  'Sosmed1':'ig= anisa_suli16',
                  'Sosmed2':'line= anisasulistya16',
                  'Sosmed3':'Fb= Anisa Sulistyaningsih',
                  'lagufavorit1':'Falling Slowly',
                  'lagufavorit2':'Fixe me up',
                  'lagufavorit3':'How to go to confession',
                  'Makananavorit1':'Mie Ayam',
                  'Makananfavorit2':'Ayam Bakar',
                  'Makananfavorit3':'rendang',
                  'Makananfavorit4':'Indomie Sambal Mata',
                  'Makananfavorit5':'Steak'
                  }
print('Identitas Diri Murni: ', identitas_diri)

#Mengubah variabel Identitas Diri
#Mengubah salah satu hobi
identitas_diri['Hobi4'] = 'Menonton Film'

#Mengubah Media Sosial
identitas_diri['Sosmed3'] = 'Linkin= Anisa Sulistyaningsih'

#Menghapus dua makanan favorit
del identitas_diri['Makananfavorit5']
del identitas_diri['Makananfavorit2']

#Menambahkan satu hobi
identitas_diri['Hobi5'] = 'Berkebun Mawar'

#Menampilkan Hasil
print('Identitas Diri Perubahan: ', identitas_diri)

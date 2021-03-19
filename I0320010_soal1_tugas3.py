#Pemograman Kaidah List

#Menginputkan 10 nama teman
nama_teman = ['Alifiana', 'Aratia', 'Audrey', 'Candrika', 'Cristin', 'Deadila', 'Desyana', 'Divana', 'Efa', 'Erika']

#Menampilkan list indeks nomor 4,6,7
print("Nama_Teman Indeks 4,6,7 : ", nama_teman[4],nama_teman[6],nama_teman[7])

#Mengganti nama teman di list 3,5,9
nama_teman[3] = 'Fajri'
nama_teman[5] = 'Erysa'
nama_teman[9] = 'Erlinda'

print("Nama Teman Baru: ", nama_teman)

#Menambahkan 2 nama teman
nama_teman.append('Ardaneswara')
nama_teman.append('Elza')
print("Nama Teman Penambahan: ", nama_teman)

#Menampilkan semua teman dengan perulangan
for teman in nama_teman:
    print(teman)

#Menampilkan panjang list nama
print(len(nama_teman))

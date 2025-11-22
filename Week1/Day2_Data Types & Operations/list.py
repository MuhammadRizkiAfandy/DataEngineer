angka = [1, 2, 3, 4]
profil = ["Fandy", 22, True]

#Operasi List
data = [10, 20, 30]

data.append(40)
data.remove(20)
print(data[0])

"""Slicing Assignment

Format umum:

list[start:end] = [data_baru]

Cara ini bisa:
menyisipkan data
mengganti data
menambah data
menghapus data"""



"""✅ 1. Menambah Data"""
"""a. append() → menambah 1 elemen di akhir"""

data = [1, 2, 3]
data.append(4)

"""b. extend() → menambah banyak elemen"""

data.extend([5, 6, 7])

"""c. insert() → menyisipkan data di posisi tertentu"""

data.insert(1, "A")




"""✅ 2. Menghapus Data"""
"""a. remove() → hapus berdasarkan isi/data"""

data.remove(3)

"""b. pop() → hapus berdasarkan index"""

data.pop(0)  # hapus index 0

"""c. del → hapus index atau range"""

del data[1]
del data[2:5]   # hapus banyak sekaligus

"""d. clear() → hapus semua isi list"""

data.clear()



"""✅ 3. Mengubah Data"""
"""Karena list mutable, kita bisa mengubah isi:"""

data[2] = 999



"""✅ 4. Menghitung / Statistik Dasar"""
"""a. len() → panjang list"""

len(data)

"""b. sum() → jumlah semua angka"""

sum([1, 2, 3])

"""c. max() → nilai terbesar"""

max([5, 10, 2])

"""d. min() → nilai terkecil"""
min([5, 10, 2])



"""✅ 5. Sorting (Mengurutkan)"""
"""a. sort() → mengurutkan secara permanen"""

data.sort()
data.sort(reverse=True)

"""b. sorted() → mengurutkan tapi tidak mengubah list asli"""

baru = sorted(data)
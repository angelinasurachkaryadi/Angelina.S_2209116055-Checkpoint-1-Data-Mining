#MERGE SORT
import random

#Fungsi Merge Sort
def merge_sort(list):
    if len(list) <= 1:
        return list
# Bagi List Menjadi 2 Bagian
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
# Gabungkan Lagi Bagian Yang Sudah Terurut
    return mergesort(left, right)


# FUngsi mergesort
def mergesort(left, right):
    result = []
    i = 0
    j = 0

# Gabungkan Elemen left dan right Secara Terurut
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
# Masukkan Elemen- Elemen Sisa (Jika Ada) Ke dalam Hasil Penggabungan
    result += left[i:]
    result += right[j:]
    return result

# Buat List Data Angka Dengan Acak
list = []
for i in range(11):
# Membuat List Data 11 Angka Dengan Secara Acak antara 1 sampai 40
    list.append(random.randint(1, 40))
# Sebelum Data Elemen Diurutkan
print("Sebelum Data Elemen Diurutkan => ", list)
sorted_list = merge_sort(list)
# Sesudah Data Elemen Diurutkan
print("Setelah Data Elemen Diurutkan => ", sorted_list)


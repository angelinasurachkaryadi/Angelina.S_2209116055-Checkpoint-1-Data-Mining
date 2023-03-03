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


# QUICK SORT
# import random

#  # Fungsi quick_sort
# def quick_sort(list_data):
#     if len(list_data) <= 1:
#         return list_data
#     pivot = list_data[len(list_data) // 2]
#     left = [x for x in list_data if x < pivot]
#     middle = [x for x in list_data if x == pivot]
#     right = [x for x in list_data if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

 # Membuat List Data 11 Angka Dengan Acak Antara 2 Sampai 60
# list = [random.randint(2, 60) for i in range(11)]
# print("Data Elemen Sebelum Diurutkan =>")
# print(list)
# # Data Elemen Sebelum Diurutkan
# sorted_data = quick_sort(list)
# # Data Eleneb Setelah Diurutkan
# print("Data Elemen Setelah Diurutkan =>")
# print(sorted_data)

# # SHELL SORT
# import random

# #Fungsi shell_sort
# def shell_sort(list):
#     y = len(list)
#     gap = y // 2

#     while gap > 0:
#         for i in range(gap, y):
#             temp = list[i]
#             j = i
#             while j >= gap and list[j - gap] > temp:
#                 list[j] = list[j - gap]
#                 j -= gap
#             list[j] = temp
#         gap //= 2

# # Membuat List Data 11 Angka Dengan Secara Acak antara 6 sampai 60
# angka = [random.randint(6, 60) for i in range(11)]
# # Data Elemen Angka Sebelum Diurutkan
# print("Elemen Data Sebelum Diurutkan => ")
# print(angka)
# shell_sort(angka)
# # Data Elemen Angka Sebelum Diurutkan
# print("Elemen Data Setelah Diurutkan => ")
# print(angka)

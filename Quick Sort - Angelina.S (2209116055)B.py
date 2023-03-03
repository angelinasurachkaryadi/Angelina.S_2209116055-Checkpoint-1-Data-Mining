# QUICK SORT
import random

 # Fungsi quick_sort
def quick_sort(list_data):
    if len(list_data) <= 1:
        return list_data
    pivot = list_data[len(list_data) // 2]
    left = [x for x in list_data if x < pivot]
    middle = [x for x in list_data if x == pivot]
    right = [x for x in list_data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

 # Membuat List Data 11 Angka Dengan Acak Antara 2 Sampai 60
list = [random.randint(2, 60) for i in range(11)]
print("Data Elemen Sebelum Diurutkan =>")
print(list)
# Data Elemen Sebelum Diurutkan
sorted_data = quick_sort(list)
# Data Eleneb Setelah Diurutkan
print("Data Elemen Setelah Diurutkan =>")
print(sorted_data)
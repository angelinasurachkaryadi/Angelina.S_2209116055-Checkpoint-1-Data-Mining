# SHELL SORT
import random

#Fungsi shell_sort
def shell_sort(list):
    y = len(list)
    gap = y // 2

    while gap > 0:
        for i in range(gap, y):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap //= 2

# Membuat List Data 11 Angka Dengan Secara Acak antara 6 sampai 60
angka = [random.randint(6, 60) for i in range(11)]
# Data Elemen Angka Sebelum Diurutkan
print("Elemen Data Sebelum Diurutkan => ")
print(angka)
shell_sort(angka)
# Data Elemen Angka Sebelum Diurutkan
print("Elemen Data Setelah Diurutkan => ")
print(angka)

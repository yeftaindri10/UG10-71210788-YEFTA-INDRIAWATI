import random


def quickSort(data, start, end):
    if start < end:
        # partisi dan dapatkan posisi pivot
        pivot_index = partition(data, start, end)
        # proses partisi sebelah kiri
        quickSort(data, start, pivot_index-1)
        # proses partisi sebelah kanan
        quickSort(data, pivot_index+1, end) 
    data.sort(reverse = True) 
    return data


def partition(data, start, end):
    # ambil salah satu sebagai pivot - (elemen terakhir)
    pivot = data[end]
    left = start
    right = end - 1
    while left <= right:
        while data[left] < pivot:
            left = left + 1
        while data[right] > pivot:
            right = right - 1
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left = left + 1
            right = right - 1
# tukar posisi data pada index left dan end
    data[left], data[end] = data[end], data[left]
    return left


def generate_list(n):
    batas_atas = 100 * n
    random_list = random.sample(range(0, batas_atas), n)
    return random_list




lst0 = [4,5,3,2,1]
lst1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
lst2 = [20,21,22,23,24,25,26,27]
lst3 = [30,29,31,33,19,20,31,21,59]
print(quickSort(lst0,0,len(lst0)-1))
print(quickSort(lst1,0,len(lst1)-1))
print(quickSort(lst2,0,len(lst2)-1))
print(quickSort(lst3,0,len(lst3)-1))
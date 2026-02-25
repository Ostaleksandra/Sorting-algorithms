import random

def quick_sort(array, left, right):
    pivot = array[random.randint(left, right)]
    i, j = left, right
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if left < j:
        quick_sort(array, left, j)
    if right > i:
        quick_sort(array, i, right)
    return array

array = [2, -7, 3, 1, 4, 6, 5, 9, 8, 7]
a = quick_sort(array, 0, len(array)-1)
print(a)
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

array = [2, -7, 3, 1, 4, 6, 5, 9, 8, 7]
a = insertion_sort(array)
print(a)
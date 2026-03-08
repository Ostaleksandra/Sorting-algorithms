def bubble_sort(array):
    N = len(array)
    for i in range(0, N-1):
        swapped = False
        for j in range(0, N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array

array = [2, -7, 3, 1, 4, 6, 5, 9, 8, 7]
a = bubble_sort(array)
print(a)

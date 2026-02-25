def selection_sort(array):
    N = len(array)
    for i in range(N):
        min_index = i
        for j in range(i + 1, N):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

array = [2, -7, 3, 1, 4, 6, 5, 9, 8, 7]
a = selection_sort(array)
print(a)


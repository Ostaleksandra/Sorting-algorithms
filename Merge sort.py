def merge_list(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result

def merge(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge(array[:middle])
        right = merge(array[middle:])
        return merge_list(left, right)



array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
a = merge(array)
print(a)
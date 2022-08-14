def insertion_sort(arr):
    for index in range(1, len(arr)):
        next_index = index
        while next_index > 0 and arr[next_index] < arr[next_index - 1]:
            arr[next_index], arr[next_index - 1] = arr[next_index - 1], arr[next_index]
            next_index -= 1
            print(arr)
    return arr


array = [22, 27, 16, 2, 18, 6]
insertion_sort(array)

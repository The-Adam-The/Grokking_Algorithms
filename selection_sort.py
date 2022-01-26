array = [6, 63, 200, 30, 50, 60, 61, 3, 4, 64, 78]


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            return smallest_index

# print(find_smallest(array))
#There is something wrong with the pop()
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        print(smallest)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort(array))

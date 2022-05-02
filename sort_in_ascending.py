import numpy as np


array = np.random.randint(0, 50, 10)
array_list = array.tolist()

print(array_list)


def ascending(arr):
    new_list = []
    i = 0
    while i < len(arr):
        num = arr[0]
        for j in range(len(arr)):
            if num >= arr[j]: 
                num = arr[j]
        new_list.append(num)
        arr.remove(num)

    return new_list

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(ascending(array_list))
print(bubbleSort(array_list))
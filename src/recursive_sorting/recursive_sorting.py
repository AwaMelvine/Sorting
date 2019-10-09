import math
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    i = 0
    x = 0
    y = 0

    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1
        i += 1

    while i <= elements - 1:
        if len(arrA) > x:
            merged_arr[i] = arrA[x]
            x += 1
        elif len(arrB) > y:
            merged_arr[i] = arrB[y]
            y += 1
        i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    middle = int(len(arr) / 2)

    left = merge_sort(arr[middle:])
    right = merge_sort(arr[:middle])

    return merge(left, right)



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

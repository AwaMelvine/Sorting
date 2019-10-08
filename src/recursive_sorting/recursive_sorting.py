import math
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    i = elements - 1
    x = len(arrA) - 1
    y = len(arrB) - 1
    done = False

    while not done:
        if arrA[x] > arrB[y]:
            merged_arr[i] = arrA[x]
            if x >= 0:
                x -= 1
        else:
            merged_arr[i] = arrB[y]
            if y >= 0:
                y -= 1

        if x < 0 or y < 0:
            done = True
        i -= 1
    merged_arr[0] = arrA[0] if arrA[0] < arrB[0] else arrB[0]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print(arr)
    # TO-DO
    if len(arr) == 0 or len(arr) == 1:
        return arr

    if len(arr) == 2:
        return merge([arr[0]], [arr[1]])

    middle = int(len(arr) / 2)
    return merge_sort(arr[middle:]) + merge_sort(arr[:middle])


print(merge_sort([2, 8, 92, 1]))


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

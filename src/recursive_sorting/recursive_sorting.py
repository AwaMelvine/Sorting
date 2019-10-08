# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    lenA = len(arrA)
    lenB = len(arrB)
    elements = lenA + lenB
    merged_arr = [0] * elements
    # TO-DO

    i = 0
    while lenB >= 0 and lenA >= 0:
        if arrA[lenA - 1 - i] > arrB[lenB - 1 - i]:
            merged_arr[elements - 1 - i] = arrA[lenA - 1]
        elif arrB[lenB - 1 - i] > arrA[lenA - 1 - i]:
            merged_arr[elements - 1 - i] = arrB[lenB - 1]
        lenB -= i
        lenA -= i
        i += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) == 0:
        return

    if len(arr) == 1:
        return arr

    return arr + merge_sort()


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

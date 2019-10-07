# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    sorted = False

    while sorted == False:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True
        if swapped == False:
            sorted = True
    return arr


print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr

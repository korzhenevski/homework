def sort_array(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def max_value(a, b):
    return a if a > b else b

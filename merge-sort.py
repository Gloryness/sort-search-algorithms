
def merge_sort(array):
    """
    Performs a merge sort on an array.
    It's quite recursive you could say
    array: list
        An array of values
    value: Any
        The value to find.
    """
    if len(array) == 1:
        return array
    
    middle = len(array) // 2

    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    print(f"\nOriginal: {array}\nLeft: {left}\nRight: {right}\n")

    a = b = c = 0

    while a < len(left) and b < len(right):
        if left[a] <= right[b]:
            array[c] = left[a]
            a += 1
        else:
            array[c] = right[b]
            b += 1
        c += 1
    
    while a < len(left):
        array[c] = left[a]
        a += 1
        c += 1
    
    while b < len(right):
        array[c] = right[b]
        b += 1
        c += 1
    
    return array

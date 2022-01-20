
def insertion_sort(array):
    """
    An insertion sort algorithm
    """
    if len(array) < 2:
        return array

    new_arr = []
    print("New List: ", new_arr)

    for element in array.copy():
        index = len(new_arr)
        stuff = []
        for x in range(len(new_arr)-1, -1, -1): # starting from index n to index 0
            if element < new_arr[x]:
                stuff.append(f"{element} < {new_arr[x]} --> index={x}")
                index = x
        new_arr.insert(index, element)
        print(new_arr, f"{element} was inserted at index {index} ({', '.join(stuff)})")
    return new_arr
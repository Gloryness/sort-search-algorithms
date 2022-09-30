
def binary_search(array, value):
    """
    Performs a binary search on an array to find a value.
    The list must be a sorted array.
    array: list
        An array of values
    value: Any
        The value to find.
    """
    array = list(enumerate(array))

    while array:
        if len(array) == 1:
            if array[0][1] == value:
                print(f"Found at index: {array[0][0]}")
                return array[0][0]
            else:
                print("Cannot Find Value")
                return None

        middle = len(array) // 2
        print(f"Testing middle index ({middle}) of array {array}")

        if array[middle][1] == value:
            print(f"Found at index: {array[middle][0]}")
            return array[middle][0]

        set1, set2 = array[:middle], array[middle:]
        print(f"Split 1: {set1}")
        print(f"Split 2: {set2}")
        if set1[-1][1] == value:
            print(f"Found at index: {set1[-1][0]}")
            return set1[-1][0]
        elif value > set1[-1][1]: # Discarding set1
            array = set2.copy()
        else: # Discarding set2
            array = set1.copy()

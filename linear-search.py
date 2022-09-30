
def linear_search(array, value):
    """
    Performs a linear search on an array to find a value.
    array: list
        An array of values
    value: Any
        The value to find.
    """
    for index, val in enumerate(array):
        print(f"Index {index}: {val} == {value} - {val == value}")
        if val == value:
            return index
    return None

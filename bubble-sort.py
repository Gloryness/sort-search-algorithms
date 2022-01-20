
def bubble_sort(array):
    """
    A bubble sort algorithm.
    """
    if len(array) < 2:
        return array


    for i in range(1, len(array)+1):
        print(f"\nPass {i}")

        changed = []
        for step in range(len(array)-1):
            res = list(sorted([array[step], array[step+1]]))
            changed.append(bool(res != [array[step], array[step+1]]))

            original = array.copy()
            original[step], original[step+1] = "*"+str(original[step]), str(original[step+1])+"*"

            array[step], array[step+1] = res

            arr = array.copy()
            arr[step], arr[step+1] = "*"+str(arr[step]), str(arr[step+1])+"*"

            print(f"Step {step+1}: {', '.join(list(map(str, original)))} --> {', '.join(list(map(str, arr)))}")

        if not any(changed) and step != len(array)-2:
            print("Stopped bubble sort algorithm due to no changes throughout whole pass.")
            break

    return array
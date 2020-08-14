# FIRST PASS SOLUTION:
"""
If I make a buffer variable I can just store the [0]th item in the list
    remove it from the list and check if it is still there since there
    should only ever be two max per the instructions. If not there I can
    just return it. If it is, then remove that one too so the sample set
    decreases. This should meet space & time requirements!
"""
def single_number(arr):
    temporary_value = None
    while len(arr)>0:
        temporary_value = arr[0]
        arr.pop(0)
        if temporary_value not in arr:
            return temporary_value
        else:
            arr.remove(temporary_value)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
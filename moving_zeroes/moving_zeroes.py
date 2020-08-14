# FIRST PASS SOLUTION:
"""
If I start at the end and just pop and append I shouldn't have to worry
    about a moving index... This lets me do it in one pass AND without
    extra space so I meet the O(1) space & time requirement!
"""
def moving_zeroes(arr):
    if (len(arr) > 1) and (0 in arr):
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr.pop(i)
                arr.append(0)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
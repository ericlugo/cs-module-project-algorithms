# FIRST PASS SOLUTION:
'''
I can use a list comprehension to create a list of max values by
    testing each set but this won't be very performant and will
    probably run out of memory at some point.
To hit the O(n) time, I need to establish a starting max and iterate
    up the array using the following logic...
    ...if the new value is larger than the current max, replace it
    ...if the current max is out of bounds remove it and get a new
        max from the current set
    ...append the current_max each round
    ...return the new list
'''
def sliding_window_max(N, k):
    current_max = max(N[:k])
    max_list = [current_max]
    for i in range(k, len(N)):
        if N[i] > current_max:
            current_max = N[i]
        elif current_max == N[i-k]:
            current_max = max(N[i-k+1:i+1])
        max_list.append(current_max)
    return max_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

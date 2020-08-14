# FIRST PASS SOLUTION:
"""
NOTE: arr[index] = product_of_everything_before * product_of_everything_after

THERE MIGHT BE A MORE ELEGANT SOLUTION BUT THIS DOES THE JOB...
    ...AND IT MEETS THE O(n) TIME & SPACE CONSTRAINTS...
    ...AND NO DIVISION!!!

I'LL TAKE IT!
"""
def product_of_all_other_numbers(arr):
    if len(arr) > 1:
        prefix_products = arr[:]
        suffix_products = arr[:]

        for i in range(1, len(arr)):
            prefix_products[i] *= prefix_products[i-1]    
        for i in range(len(arr)-2, -1, -1):
            suffix_products[i] *= suffix_products[i+1]
        for i in range(len(arr)):
            if i == 0:
                arr[i] = suffix_products[i+1]
            elif i == len(arr)-1:
                arr[i] = prefix_products[i-1]
            else:
                arr[i] = prefix_products[i-1]*suffix_products[i+1]
    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

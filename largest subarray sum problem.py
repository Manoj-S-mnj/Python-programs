def largest_subarray_sum(arr):
    if not arr:
        return 0
    
    current_max = global_max = arr[0]
    
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)
    
    return global_max

# Test case
arr = [-2,-3,4,-1,-2,1,5,-3]
print("The largest subarray sum is:", largest_subarray_sum(arr))

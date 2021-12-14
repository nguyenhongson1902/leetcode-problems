def maxSubArray(nums):
    # brute force solution, didn't pass all test cases
    
    tmp = list()
    max_subarray_sum = nums[0]
    
    for i in range(len(nums)-1):
        tmp.append(nums[i])
        if sum(tmp) > max_subarray_sum:
            max_subarray_sum = sum(tmp)
        for j in range(i+1, len(nums)):
            tmp.append(nums[j])
            if sum(tmp) > max_subarray_sum:
                max_subarray_sum = sum(tmp)
            
        tmp = list()
    if nums[-1] > max_subarray_sum:
        max_subarray_sum = nums[-1]
    
    return max_subarray_sum


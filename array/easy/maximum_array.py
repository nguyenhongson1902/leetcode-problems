def maxSubArray(nums):
    # brute force solution, didn't pass all test cases
    
    # tmp = list()
    # max_subarray_sum = nums[0]
    
    # for i in range(len(nums)-1):
    #     tmp.append(nums[i])
    #     if sum(tmp) > max_subarray_sum:
    #         max_subarray_sum = sum(tmp)
    #     for j in range(i+1, len(nums)):
    #         tmp.append(nums[j])
    #         if sum(tmp) > max_subarray_sum:
    #             max_subarray_sum = sum(tmp)
            
    #     tmp = list()
    # if nums[-1] > max_subarray_sum:
    #     max_subarray_sum = nums[-1]
    
    # return max_subarray_sum

    # optimal solution, time complexity O(n)
    sum_current = nums[0]
    sum_global = nums[0]
    
    for i in range(1, len(nums)):
        sum_current = max(nums[i], sum_current + nums[i])
        
        if sum_current > sum_global:
            sum_global = sum_current
    
    return sum_global


case1 = [-2,1,-3,4,-1,2,1,-5,4]
print('Expected output:', 6)
print('Actual output:', maxSubArray(case1))




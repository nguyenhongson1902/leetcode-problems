def searchInsert(nums, target):
    # Data structure: Array
    # Algorithm: Binary search (using iterative implementation)
    # Time complexity: O(log(n))

    left = 0
    right = len(nums)-1
    if target > nums[-1]:
        return len(nums)
    else:
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        # if we reach here, it means the target element was not in the list
        return left # the `left` would be the position `target` takes if it was in the list


t = [1,3,5,6]
print('Expected output:', 2)
print('Actual output:', searchInsert(t, 5))
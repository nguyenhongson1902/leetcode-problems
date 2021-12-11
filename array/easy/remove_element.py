def removeElement(nums, val):
    # Move the elements to be removed to the end of the array
    # My solution
    i = 0
    while i < len(nums):
        if nums[i] == val:
            j = i + 1
            while j < len(nums):
                tmp = 0
                if nums[j] != val:
                    # swap nums[i] and nums[j]
                    tmp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = tmp
                    break
                else:
                    j += 1
            i += 1
        else:
            i += 1
    k = len(nums)
    for i in range(len(nums)):
        if nums[i] == val:
            k = i
            break
    return k


if __name__ == '__main__':
    case1 = [0,2,3,4,5,3,1,0]
    print("Expected output:", 6)
    print("Actual output:", removeElement(case1, val=3))
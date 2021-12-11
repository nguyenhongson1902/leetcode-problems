def remove_duplicates(nums):
    if nums:
        tmp = [nums[0]]
    else:
        tmp = list()
    i = 1
    while i < len(nums):
        if nums[i] != nums[i-1]:
            tmp.append(nums[i])
        i += 1
    k = len(tmp)
    nums[:k] = tmp
    return k

t = [0,0,0,0,0,1,2,2,3,3,4,4]
print('Expected output:', 5)
print('Actual output:', remove_duplicates(t))
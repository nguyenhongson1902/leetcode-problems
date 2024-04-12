from typing import List
# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_products = {}
        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix_products[i] = 1
        #         continue
        #     product = prefix_products[i-1] * nums[i-1]
        #     prefix_products[i] = product
        # # print(prefix_products)

        # suffix_products = {}
        # for i in range(len(nums)):
        #     if i == 0:
        #         suffix_products[len(nums) - 1] = 1
        #         continue
        #     product = suffix_products[len(nums) - i] * nums[-i]
        #     suffix_products[len(nums) - i - 1] = product
        # # print(suffix_products)

        # result = []
        # for i in range(len(nums)):
        #     result.append(prefix_products[i] * suffix_products[i])
        
        # return result
# Time: O(n)
# Space: O(n)

        result = [1] * len(nums)
        # Compute prefix
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # print(result)

        # Compute suffix
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        # print(result)
        return result

# Time: O(n)
# Space: O(1)


            
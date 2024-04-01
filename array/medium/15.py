from typing import List
# https://leetcode.com/problems/3sum/description/
# ThreeSum


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # Time: O(n^2)
        # # Space: O(n^2)
        # result = []
        
        # for i in range(len(nums)):
        #     hash_map = {}
        #     residue_sum = 0 - nums[i]
        #     # Coming back to the two sum problem
        #     for j in range(i + 1, len(nums)):
        #         if residue_sum - nums[j] in hash_map:
        #             sorted_answer = sorted([nums[i], nums[j], residue_sum - nums[j]])
        #             if sorted_answer not in result:
        #                 result.append(sorted_answer)
        #         else:
        #             hash_map[nums[j]] = j
        
        # return result

        # Time: O(n^2)
        # Space: O(n) or O(1)

        sorted_nums = sorted(nums)
        # print(sorted_nums)
        result = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            # print("i:", i)
            begin, end = i + 1, len(sorted_nums) - 1
            while begin < end:
                three_sum = sorted_nums[begin] + sorted_nums[end] + sorted_nums[i]
                # print(three_sum)
                if three_sum > 0:
                    end -= 1
                elif three_sum < 0:
                    begin += 1
                else:
                    result.append([sorted_nums[i], sorted_nums[begin], sorted_nums[end]])
                    begin += 1
                    while sorted_nums[begin] == sorted_nums[begin-1] and begin < end:
                        begin += 1
        return result


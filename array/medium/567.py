# Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

import string
import math


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # k, n = len(s1), len(s2)
        # for i in range(n - k + 1):
        #     if sorted(s2[i:i+k]) == sorted(s1):
        #         return True
        # return False
        # Time complexity: O(n) or O(nklog(k)), k <= 26
        # Space complexity: O(1)
        
        # Solution 2 (why is it not accepted?), time O(nk), n = len(s2), k = len(s1), space O(1)
        # def helper():
        #     result = {}
        #     n = 2
        #     count = 0
        #     while n >= 2 and count < 26:
        #         is_prime = True
        #         for i in range(2, int(math.sqrt(n)) + 1):
        #             if n % i == 0:
        #                 is_prime = False
        #         if is_prime:
        #             result[string.ascii_lowercase[count]] = n
        #             count += 1
        #         n += 1
        #     return result
        
        # def is_permutation(a, b):
        #     '''Is a a permutation of b?'''
        #     assert len(a) == len(b)
        #     mul1, mul2 = 1, 1
        #     for i in range(len(a)):
        #         mul1 *= char2prime[a[i]]
        #         mul2 *= char2prime[b[i]]
            
        #     return True if mul1 == mul2 else False

        # char2prime = helper()
        
        # k, n = len(s1), len(s2)
        # for i in range(n - k + 1):
        #     if is_permutation(s2[i:i+k], s1):
        #         return True
        # return False

        # def is_permutation(a, b):
        #     assert len(a) == len(b)
        #     freq_a, freq_b = {}, {}
        #     for i in range(len(a)):
        #         freq_a[a[i]] = freq_a.get(a[i], 0) + 1
        #         freq_b[b[i]] = freq_b.get(b[i], 0) + 1

        #     for k in freq_a.keys():
        #         if k not in freq_b.keys():
        #             return False
        #         if freq_a[k] != freq_b[k]:
        #             return False
        #     return True

        # k, n = len(s1), len(s2)
        # for i in range(n - k + 1):
        #     if is_permutation(s2[i:i+k], s1):
        #         return True
        # return False

        # Edge case
        if len(s1) > len(s2):
            return False

        freq_1, freq_2 = {}, {}
        for c in string.ascii_lowercase: # O(1)
            freq_1[c] = 0
            freq_2[c] = 0

        for c in s1: # O(k), k = len(s1)
            freq_1[c] += 1

        for c in s2[:len(s1)]: # O(k)
            freq_2[c] += 1

        if freq_2 == freq_1: # constant because of considering only 26 letters
            return True

        freq_2[s2[0]] -= 1 # reduce the left before setting left=1
        left, right = 1, len(s1)
        while right < len(s2): # O(n)
            freq_2[s2[right]] += 1 # increase the right
            if freq_2 == freq_1:
                return True
            else:
                freq_2[s2[left]] -= 1 # reduce the left
                left += 1
                right += 1
        return False
        # Time complexity: O(n) + O(k), n = len(s2), k = len(s1)
        # We only consider len(s1) < len(s2), so the time complexity would be O(n)
        # Space complexity: O(1)
        


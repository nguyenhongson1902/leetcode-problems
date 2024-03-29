# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        begin, end = 0, 1
        max_length = 1

        while end < len(s):
            if len(set(s[begin:(end + 1)])) == len(s[begin:(end + 1)]):
                current_length = end - begin + 1
                max_length = max(max_length, current_length)
            else:
                begin += 1
            end += 1
        
        return max_length
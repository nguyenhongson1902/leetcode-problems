# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring Without Repeating Characters

# The first time
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
    
# The second time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left, right = 0, 0
        max_len = 0
        char_set = set()
        while right < len(s):
            curr_len = right - left + 1
            if s[right] not in char_set:
                char_set.add(s[right])
                max_len = max(max_len, curr_len)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1
            
        return max_len
    # Time complexity: O(n), n = len(s)
    # Space complexity: O(n), worst case: every character is UNIQUE

    # if len(s) <= 1:
        #     return len(s)

        # left, right = 0, 0
        # max_len = 0
        # char_set = set()
        # while right < len(s):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        #     curr_len = right - left + 1
        #     char_set.add(s[right])
        #     max_len = max(max_len, curr_len)
        #     right += 1
            
        # return max_len
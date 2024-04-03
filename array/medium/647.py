# Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/
# Two pointers


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # Counting palindrome subtrings at odd positions
        curr = 0
        while curr < len(s):
            left, right = curr, curr
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            curr += 1
        
        # Counting palindrome subtrings at even positions
        curr = 0
        while curr < len(s):
            left = curr
            right = left + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            curr += 1
        
        return count
        
            
            


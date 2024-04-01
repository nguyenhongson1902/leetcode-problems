# https://leetcode.com/problems/valid-palindrome/description/
# Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for c in s.lower():
            if c.isalnum():
                s_new += c
        # print(s_new)
        begin, end = 0, len(s_new) - 1
        while begin < end:
            if s_new[begin] != s_new[end]:
                return False
            begin += 1
            end -= 1
        return True
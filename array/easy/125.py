# https://leetcode.com/problems/valid-palindrome/description/
# Valid Palindrome


# The first time
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

# The second time
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = s.lower()
        tmp = "".join(tmp.split(" "))
        tmp = "".join([c for c in tmp if c.isalnum()])

        left, right = 0, len(tmp) - 1
        while left <= right and tmp[left] == tmp[right]:
            left += 1
            right -= 1            
        
        return True if left > right else False
        # Time complexity: O(n), n = len(s)
        # Space complexity: O(n), n = len(s) because we use a temporarily processed string
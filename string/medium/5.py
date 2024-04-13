# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        for i in range(len(s)):
            # Substring's length is odd
            tmp = s[i]
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    tmp = s[left] + tmp + s[right]
                    left -= 1
                    right += 1
                    if len(tmp) > len(result):
                        result = tmp
                else:
                    break
            
            # Substring's length is even
            tmp2 = ''
            left, right = i - 1, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    tmp2 = s[left] + tmp2 + s[right]
                    left -= 1
                    right += 1
                    if len(tmp2) > len(result):
                        result = tmp2
                else:
                    break
        return result

# Time: O(n^2)
# Space: O(1)

# Brute force: For each substring, we check if it is a palindrome or not
# Traverse through each substring take O(n^2) time
# Check if a substring is a palindrome takes O(n) time
# So, it takes O(n^3) time complexity for naive approach
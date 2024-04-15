# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        # s is valid only when len(s) is odd
        if len(s) % 2 != 0:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            else:
                # if stack is empty and the s[i] is one of the closed brackets, return False
                if not stack:
                    return False
                else:
                    last_char = stack.pop()
                    # If there is a mismatch, return False
                    if last_char + s[i] not in ["()", "[]", "{}"]:
                        return False
        
        # if stack is not empty, e.g. "((([[["
        if stack:
            return False
        return True

        # Time: O(n)
        # Space: O(n)

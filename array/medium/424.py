# Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_len = 0
        freq = {}
        right_increased = False
        while right < len(s):
            curr_len = right - left + 1
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                if right_increased:
                    freq[s[right]] += 1
            # print("freq", freq)
            # print("left", left, "right", right)
            max_freq_char = max(freq, key=freq.get) # most occurred letter
            max_freq = freq[max_freq_char] # most occurrences
            if curr_len - max_freq <= k:
                max_len = max(max_len, curr_len)
                right += 1
                right_increased = True
            else:
                freq[s[left]] -= 1
                left += 1
                right_increased = False
        return max_len
        # Time complexity: O(26n), n = len(s), because we have 26 possible upper case letters

        # left, right = 0, 0
        # max_len = 0
        # freq = {}
        # while right < len(s):
        #     freq[s[right]] = freq.get(s[right], 0) + 1
        #     while (right - left + 1) - max(freq.values()) > k:
        #         freq[s[left]] -= 1
        #         left += 1
        #     max_len = max(max_len, right - left + 1)
        #     right += 1
        # return max_len


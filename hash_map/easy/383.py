# Ransom Note
# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for i, c in enumerate(magazine):
            if c not in hash_map:
                hash_map[c] = [i]
            else:
                hash_map[c].append(i)

        count_check = 0
        for i, c in enumerate(ransomNote):
            magazine_indices = hash_map.get(c, -1)
            if magazine_indices == -1:
                return False
            else:
                if magazine_indices:
                    magazine_indices.pop()
                    count_check += 1
                else:
                    return False
        
        return True if count_check == len(ransomNote) else False

        # Time: O(n + m), n = len(ransomNote), m = len(magazine)
        # Space: O(m), m = len(magazine)

        # The basic approach is to loop through every character in ransomNote. For each character, check if there is that character in magazine. If there is, delete the character in magazine. If there is not, return False. Finally, if there's nothing happen, return True.
        # Time: O(nm), n = len(ransomNote), m = len(magazine)
        # Space: O(m), m = len(magazine)
        

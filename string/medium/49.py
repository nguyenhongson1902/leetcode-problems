from typing import List
import string

# Group Anagrams
# https://leetcode.com/problems/group-anagrams/


class Solution:
    def is_prime(self, n):
        upper_bound = int(n**0.5)
        for i in range(2, upper_bound + 1):
            if n % i == 0:
                return False
        return True

    def generate_primes(self, n_primes=26):
        result = []
        n = 2
        while n > 0 and len(result) < n_primes:
            if self.is_prime(n):
                result.append(n)
            n += 1
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        primes = self.generate_primes() # 26 primes corresponding to 26 lowercase characters
        hash_map = {}
        for i, c in enumerate(string.ascii_lowercase):
            hash_map[c] = primes[i]
        
        hash_map2 = {}
        for s in strs:
            product = 1
            for c in s:
                product *= hash_map[c]
            if product in hash_map2:
                hash_map2[product].append(s)
            else:
                hash_map2[product] = [s]
        
        for k in hash_map2.keys():
            result.append(hash_map2[k])

        return result
            
# Time: O(n)
# Space: O(1)
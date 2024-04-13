# Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

import string


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

    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) # Easy peasy, Time: O(nlog(n) + nlog(m)), n = len(s), m = len(t), Space: O(1)
        primes = self.generate_primes()
        hash_map = {}
        for i, c in enumerate(string.ascii_lowercase):
            hash_map[c] = primes[i]

        product_s = 1
        for c in s:
            product_s *= hash_map[c]
        
        product_t = 1
        for c in t:
            product_t *= hash_map[c]
        
        return product_s == product_t

        # Time: O(n + m), n = len(s), m = len(t)
        # Space: O(1)
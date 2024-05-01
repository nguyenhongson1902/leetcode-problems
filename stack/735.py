from typing import List
# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]
                if diff > 0: # top wins over asteroid
                    asteroid = 0 # destroy asteroid
                elif diff < 0: # asteroid wins over top
                    stack.pop() # destroy top
                else: # top == asteroid
                    asteroid = 0 # destroy asteroid
                    stack.pop() # destroy top
            if asteroid:
                stack.append(asteroid)
            
        return stack
        # Time: O(n), n = #asteroids
        # Space: O(n)

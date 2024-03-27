# https://leetcode.com/problems/minimum-window-substring/solutions/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems/

def minWindow(s, t):
    map = [0] * 128
    for c in t:
        map[ord(c)] += 1
    counter = len(t)
    begin = 0
    end = 0
    d = float('inf')
    head = 0
    while end < len(s):
        if map[ord(s[end])] > 0:
            counter -= 1
        map[ord(s[end])] -= 1
        end += 1
        while counter == 0:
            if end - begin < d:
                # d = end - (head == begin)
                d = end - head
                head = begin
            map[ord(s[begin])] += 1
            if map[ord(s[begin])] > 0:
                counter += 1
            begin += 1
    return "" if d == float('inf') else s[head:head + d]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))


def minWindow(s, t):
    # Initialize a map to keep track of characters in t
    char_map = [0] * 128
    for char in t:
        char_map[ord(char)] += 1

    # Initialize variables
    counter = len(t)
    begin = 0
    end = 0
    min_length = float('inf')
    head = 0

    # Iterate over the string s
    while end < len(s):
        # If the current character is in t, decrement the counter
        if char_map[ord(s[end])] > 0:
            counter -= 1
        # Decrement the map value for the current character
        char_map[ord(s[end])] -= 1
        # Move the end pointer
        end += 1

        # While all characters of t are included in the current window
        while counter == 0:
            # If the current window is smaller than the smallest found so far
            if end - begin < min_length:
                min_length = end - begin
                head = begin
            # Increment the map value for the character at the begin position
            char_map[ord(s[begin])] += 1
            # If this character is in t, increment the counter
            if char_map[ord(s[begin])] > 0:
                counter += 1
            # Move the begin pointer
            begin += 1

    # Return the smallest window or an empty string if no such window is found
    return "" if min_length == float('inf') else s[head:head + min_length]


"""
This template uses the sliding window technique. It maintains two pointers (begin and end) to represent a window in s. It expands the window until it contains all characters of t and then shrinks it from the left until it no longer contains all characters of t. It keeps track of the smallest window that contains all characters of t.
"""
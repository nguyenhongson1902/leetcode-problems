def reverse(s, i=0):
    """
    Do not return anything, modify s in-place instead.
    Input:
        s: A list of characters
    Output:
        None
    """
    n = len(s[i:len(s)-i])
    if n >= 2:
        s[i], s[-i-1] = s[-i-1], s[i]
        i += 1
        reverse(s, i)

s = list('hello')
reverse(s)
print(s)
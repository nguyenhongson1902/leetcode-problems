# Explaination: https://www.code-recipe.com/post/container-with-most-water

# My implementation
def max_area(height):
    left = 0
    right = len(height) - 1
    tmp = [(right-left) * min(height[left], height[right])]
    while left < right:
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
        tmp.append((right-left) * min(height[left], height[right]))
    
    return max(tmp)

if __name__ == '__main__':
    test_1 = [1,8,6,2,5,4,8,3,7]
    print('Expected output:', 49)
    print('Output:', max_area(test_1))

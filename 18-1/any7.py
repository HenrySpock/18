NUMS1 = [1, 2, 7, 4, 5]
NUMS2 = [1, 2, 4, 5]
NUMS3 = [1, 2, 4, 5, 777]

def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    for num in nums:
        if num == 7: 
            return True
    
    return False

print("should be true", any7(NUMS1))
print("should be false", any7(NUMS2))
print("what will 777 be?", any7(NUMS3))

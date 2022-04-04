NUMS1 = [2, 3, 4, 5, 6]
NUMS2 = [3, 4, 5]
NUMS3 = [1, 3, 5]

def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    not_one = 1

    for num in nums:
        if num % 2 == 0:
            not_one = not_one * num

    return not_one

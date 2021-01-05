"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.
"""
# TEMPLATE #2 example
# import List from typing to support hinting in function definition 
from typing import List


class Solution:
    def find_min(nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        
        left, right = 0, len(nums)-1
        min = 0
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            #print(nums[mid])
            elif nums[mid] > nums[mid-1]:
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                return nums[mid]
        # post processing ( required , loop ends when 1 element left ) ?

    # TEST 
    nums = [4,5,6,7,0,1,2]
    print(find_min(nums))
    # expected output - 0

    nums = [3,4,5,1,2]
    print(find_min(nums))
    # 1
    nums = [2, 1]
    print(find_min(nums))
    # 1
    nums = [11,13,15,17]
    print(find_min(nums))
    # 11
    nums = [2,3,1]
    print(nums)
    print(find_min(nums))
    #1

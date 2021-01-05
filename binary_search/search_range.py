"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""
# TEMPLATE #3 example
# import List from typing to support hinting in function definition 
from typing import List

class Solution:
    def searchRange(nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        if len(nums) == 0:
            return [start, end]
        if len(nums) == 1:
            if nums[0] == target:
                start, end = 0, 0
            return [start, end]
        if len(nums) == 2:
            if nums[0] == target:
                start = 0
                if nums[1] == target:
                    end = 1
                else:
                    end = 0
                return [start, end]
            elif nums[1] == target:
                start, end  = 1, 1
            return [start, end]

        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            print('left', left, 'right - ',right)
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                l = len(nums[:mid])
                for i in range(l):
                    while nums[mid] == nums[l-i-1]:
                        if nums[l-i-1] == nums[mid]:
                            start = l-i-1
                for i in range(len(nums[mid:])):
                    while nums[mid] == nums[i]:
                        if nums[i] == target:
                            end = i
                return[start, end]
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            start, end = left, left
        elif nums[right] == target:
            start, end = right, right
        return [start, end]

    # TEST 
    nums = [5,7,7,8,8,10]
    target = 8
    print(searchRange(nums, target))
    # expected output - [3,4]

    nums = [5,7,7,8,8,10]
    target = 6
    print(searchRange(nums, target))
    # [-1,-1]

    nums = []
    target = 0
    print(searchRange(nums, target))
    # [-1,-1]

    nums = [1]
    target = 1
    print(searchRange(nums, target))
    # [0, 0]

    nums = [2,2]
    target = 2
    print(searchRange(nums, target))
    # [0, 1]

    nums = [1,3]
    target = 1
    print(searchRange(nums, target))
    # [0, 1]

    nums = [1,4]
    target = 4
    print(searchRange(nums, target))
    # [1, 1]

    nums = [1,2,3]
    target = 1
    print(nums, len(nums))
    print(searchRange(nums, target))
    # [0, 0]

    nums = [1,2,3,3,3,3,4,5,9]
    target = 3
    print(nums, len(nums))
    print(searchRange(nums, target))
    # [2, 5]



    

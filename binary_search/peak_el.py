# TEMPLATE #2 example
# A peak element is an element that is greater than its neighbors.
# my solution  beats 65:
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len (nums) == 0:
            return -1
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
        return left

# other solution - runtime beats 23% with 
class Solution2(object):
    def findPeakElement(self, nums):
        if len(nums)==1 or nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return len(nums)-1
        start=1
        end=len(nums)-2
        while end>=start:
            mid=(start+end)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                start=mid+1
            elif nums[mid-1]>nums[mid]:
                end=mid-1

# one more solution = beats 25 %
class Solution3:
    def recurse(self,start,end,nums):
        ## Getting the index of the middle element
        mid=(start+end)//2
        ## If the current mid pointer is at the first element 
        ## and if the first element is greater than           
        ## the second element, then return the index.
        if mid==0 and nums[mid]>nums[mid+1]:
            return mid
        ## If the mid pointer is at the last element and 
        ## its the peak element then return the last index.
        if mid==len(nums)-1 and nums[mid]>nums[mid-1]:
                return mid
        ## If the middle element is the peak element then return
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid
        ## Else, based on the condition, search the reduced search space for the peak element.
        else:
            if mid>0 and nums[mid]<nums[mid-1]:
                return self.recurse(start,mid-1,nums)
            elif mid<(len(nums)-1) and nums[mid]<nums[mid+1]:
                return self.recurse(mid+1,end,nums)
                
            
    def findPeakElement(self, nums: List[int]) -> int:
        ## If the length of array is just 1, then return the first element as peak element
        if len(nums)==1:
            return 0
        
        return self.recurse(0,len(nums),nums)
	
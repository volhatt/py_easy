# TEMPLATE #1
#  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0, 1, 2, 4, 5, 6, 7] might become[4, 5, 6, 7, 0, 1, 2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.


def search(nums, target):
    left, right = 0, len(nums)-1
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right

    while left <= right:
        mid = (left + right) // 2
        print(mid, left, right)
        if nums[mid] == target:
            return mid

        # if left half is in order
        if nums[left] <= nums[mid]:
            print("left < mid")
            # if target on the left
            if nums[left] <= target and nums[mid] >= target:
                right = mid - 1
            # if target is not in the left half
            else:
                left = mid + 1
        # if right half is sorted
        else:
            print("left > mid")
            # if target is in the right half
            if nums[mid] < target and nums[right] >= target:
                left = mid + 1
            # if target is not in the right half
            else:
                right = mid - 1
    return -1


print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))

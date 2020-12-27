# TEMPLATE #2 example
"""
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        Find the lowest version in n that returns from isBadVersion API as true
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        if n == 1:
            return 1
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            # check if mid is bad version
            if isBadVersion(mid):
                # check if mid is first bad version
                if not isBadVersion(mid-1):
                    return mid
                # if mid is bad and previous is bad so target is on the left ( smaller )
                right = mid
            else:
                # if mid is not bad but next is bad - it will be first bad
                if isBadVersion(mid+1):
                    return mid + 1
                # if not, then target is on the right
                else:
                    left = mid+1

        return -1
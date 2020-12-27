# TEMPLATE #1
#  implement int sqrt(int x)
# compute and return the square root of x, where x is garanteed to be a non-negative integer.
class Solition:

    # solution with binary search
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # approach to use binary search to find the largest int whose square is <= than x

        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        #left > right 
        return right

    # my solustion 
    def mySolution(self, x):
        if x < 1:
            return 0
        elif x < 4:
            return 1
        left, right = 0, x
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
                ans = mid
            elif mid ** 2 > x:
                right = mid -1
        return ans

    # approach Newton's method
    def newton(self, x):
        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2
        return (int(result))


test = Solition()
print(test.mySqrt(8))
print(test.mySolution(8))
print(test.newton(8))


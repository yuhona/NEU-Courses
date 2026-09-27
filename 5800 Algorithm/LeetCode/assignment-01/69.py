class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest k, k * k <= x
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2

            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        # left > right
        # right <= mid < left
        # right * right <= x < left * left
        return right
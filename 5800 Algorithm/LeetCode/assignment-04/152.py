class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # nums = [2,3,-2,4] [2] [2,3] [2,3,-2] [2,3,-2,4] 
        # brute force
        # max_p[0]: f[0][0]
        # max_p[1]: f[0][1]  f[1][1]
        # max_p[2]: f[0][2]  f[1][2]  f[2][2]
        # max_p[3]: f[0][3]  f[1][3]  f[2][3]  f[3][3]
        # for l in range(n):
        #      for r in range(l, n):
        #           f[l][r] = f[l][r - 1] * nums[r]
        # overlaping subproblems and optimal substruture
        # dp: 1. define the state
        # max_p[r] : the max product of subarray that ends at r
        # min_p[r] : the min product of subarray that ends at r
        # 2. state transition
        # curr: prev
        # max_p[r] => max_p[r - 1]
        # case1: only have nums[r]
        # case2: extend the previous subarray, max_p[r - 1] * nums[r]/ min_p[r - 1] * nums[r]
        # [2,3,  -2,  -4]
        #    6, -12,  48

        n = len(nums)

        max_p = [1] * n
        min_p = [1] * n

        max_result = nums[0]

        for r in range(n):
            max_p[r] = max(nums[r], max_p[r - 1] * nums[r], min_p[r - 1] * nums[r])
            min_p[r] = min(nums[r], max_p[r - 1] * nums[r], min_p[r - 1] * nums[r])

            max_result = max(max_result, max_p[r])

        return max_result



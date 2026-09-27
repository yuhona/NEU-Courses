class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # nums = [1,3,5,6], target = 0
            #         l m   r
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        # nums = [1,3,5,6], target = 2
        #           l: the first ele that is greater than the target
        #         r: the last ele that is smaller than the target 
        return left

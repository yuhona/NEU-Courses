class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # nums = [4,5,6,7,0,1,2]
            #         l.          r
            #.              m
            # left part is in ordered
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right part is in ordered
            # nums = [6,7,0,1,2,4,5]
            #         l.          r
            #.              m
            elif nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
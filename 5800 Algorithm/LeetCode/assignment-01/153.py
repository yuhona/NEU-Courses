class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # [11,13,15,17]
            if nums[left] <= nums[right]:
                return nums[left]

            mid = (left + right) // 2
            #[4,5,6,7,0,1,2]
            # l.    m.    r
            if nums[left] < nums[mid]:
                left = mid + 1
            #[6,7,0,1,2,4,5]
            # l.    m.    r
            #[3,1,2]
            # l m r
            # l 
            # r
            elif nums[mid] < nums[right]:
                right = mid



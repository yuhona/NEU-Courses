class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {} # count the frequency of the ele

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        start = 0
        for i in range(3):
            cnt = freq.get(i, 0)
            # i = 0, cnt = 2, nums[0, 2] = [0, 0]
            nums[start: start + cnt] = [i] * cnt
            start += cnt
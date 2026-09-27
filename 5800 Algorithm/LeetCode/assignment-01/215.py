import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #find the kth largest element in the array. => 
        # 1 main a minimum heap of k ele in it
        # 2 push all the ele in nums, if len(heap) > k, pop the heap
        # 3 return the top of the heap
        # nums = [3,2,1,5,6,4], k = 2
        # [1,2,3,4,5,6]
        '''
        maintain a minimum heap of k ele in it
        5
    /       \
    6  
        nums = [3,2,3,1,2,4,5,5,6], k = 4    
        4
    /       \
   5        5
/
6
        '''
        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
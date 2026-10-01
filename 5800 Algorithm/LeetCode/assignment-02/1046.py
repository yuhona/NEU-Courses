'''
for each tern:
    choose the heaviest two stones:
        compare y and x:
            if y > x:
                add a new stone y-x
sort: O(n log n)
resort: O(n * nlog n) = O(n^2 logn)
the heap: 
'''
import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -x)

        while len(heap) > 1:
            y = -heap[0]
            heapq.heappop(heap)
            x = -heap[0]
            heapq.heappop(heap)
            if y - x > 0:
                heapq.heappush(heap, - (y - x))
        
        return 0 if len(heap) == 0 else -heap[0]
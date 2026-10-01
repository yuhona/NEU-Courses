class KthLargest:
    '''
    keep track of the kth highest test score in real-time
    add: 
        1. add the new score val
        2. find the kth largest ele
            push the ele into the heap
            if the size of the heap > k:
                pop the top of the heap
            return the top 
        [4, 5, 8, 2], k = 3
        4
    /       \
    5       8
   O(n logn)
    '''
    def __init__(self, k: int, nums: list[int]):#self : instance
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
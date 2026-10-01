class Solution:
    '''
    [[3,3],[5,-1],[-2,4]], k = 2
     √18    √26     √20
    1. calculate the distance for all points, d = x*x + y*y
    2. sort all the points first by the distance , x, y
    3. return the top k [x, y]
    '''
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # heap = []#O(n logk)
        # for x, y in points:
        #     distance = x * x + y * y
        #     heapq.heappush(heap, (-distance,x, y))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return [[x, y] for distance, x, y in heap]
        dic_distance = []
        for x, y in points:
            d = x * x + y * y
            dic_distance.append((d, x, y))
        dic_distance.sort()#O(n logn)

        return [[x, y] for d, x, y in dic_distance[:k]]
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        '''
        edges = [[0,1,0,1],[1,2,2,5]]
        edge 0->1: [0, 1]
        edge 1->2: [2, 5]
        start node 0:
        -> t = 0, 0 <= t < 1, travel along 1, new_time = 0 + 1 = 1
        -> t = 1, t < [2,5], wait, travel along 2, new_time = 2 + 1 = 3

        find the shortest distance form start to end
        1. Dijkstra: no negtive weight
        2. Bellman ford
        3. BFS, we have weight is not 1

        # Dijkstra
        1. built the adjancancy list
        2. extract the min distance, use this node to relax all its neighbour
        O(V*logV) = O(n^2)
        '''
        # base of 1
        if n == 1:
            return 0

        # build the adjancancy list
        graph = {}
        for u, v, start, end in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, start, end))

        # 2. do Dijkstra
        # start from (0, 0) (arrive time, node)
        heap = [(0, 0)]
        # record the dis from source to it
        INF = math.inf
        dis = [INF] * n
        dis[0] = 0

        while heap:
            # extract
            arrive_time, node = heapq.heappop(heap)
            # ingnore the old one
            if arrive_time > dis[node]:
                continue

            # reach the end
            if node == n - 1:
                return dis[node]

            # relax all the neighbours
            for nex, start, end in graph.get(node, []):
                # if we arrive early: wait until the start
                # if we arrive on time: + 1
                # if we arrive late: closed
                if arrive_time < start:
                    new_time = start + 1
                elif arrive_time <= end:
                    new_time = arrive_time + 1
                else:
                    continue
                
                if new_time < dis[nex]:
                    dis[nex] = new_time
                    heapq.heappush(heap, (dis[nex], nex))
        return -1

        
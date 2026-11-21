class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        '''
        [1, 0, 0]
        [1, 1, 0]
        [1, 1, 0]
        '''
        # base case
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # find the shortest clear path
        # 1. Dijkstra O(V log V + E * del) 
        # 2. BFS O(V + E) = O(n^2)
        # 3. dp, not deal with circles

        # BFS, use queue
        queue = deque([(0, 0, 1)])
        # mark it 
        visited = [[0]*n for _ in range(n)]
        visited[0][0] = 1

        directions = [
            (0, -1), (0, 1), (-1, 0), (1, 0),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        while queue:
            # get the front of the queue
            x, y, distance = queue.popleft()

            # reach the end
            if x == n - 1 and y == n - 1:
                return distance

            # visite all the neighbours
            for dx, dy in directions:
                # check if is valid and unvisited
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and visited[nx][ny] == 0:
                    # mark it and push into the queue
                    visited[nx][ny] = 1
                    queue.append((nx, ny, distance + 1))
        return -1



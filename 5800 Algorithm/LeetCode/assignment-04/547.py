class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #   | 1 2 3
        # 1 | 1 1 0
        # 2 | 1 1 0
        # 3 | 0 0 1
        # province: the connected components
        # dfs: visit all the connected nodes, find a province
        n = len(isConnected)
        provinces = 0
        visited = [0] * n

        # stack
        stack = []

        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                provinces += 1
                stack.append(i)

                while stack:
                    curr = stack.pop()

                    for j in range(n):
                        if isConnected[curr][j] and not visited[j]:
                            visited[j] = 1
                            stack.append(j)

        return provinces
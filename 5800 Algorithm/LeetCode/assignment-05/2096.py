class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # 1. divide can not be used
        # 2. try prefix product and the suffix produ
        #  p[k] = prefix[k] * suffix[k]
        # prefix[k] = grid[0] * ... * grid[k - 1]
        # suffix[k] = grid[k + 1] * .... * grid[n - 1]
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        total = n * m

        prefix = [1] * total
        # calculate the prefix
        for k in range(1, total):
            # prefix[k] = grid[0] * ... * grid[k - 1]
            i, j = (k - 1) // m, (k - 1) % m
            prefix[k] = prefix[k - 1] * grid[i][j] % MOD

        suffix = [1] * total
        # calculate the suffix
        for k in range(total - 2, -1, -1):
            # suffix[k] = grid[k + 1] * .... * grid[n - 1]
            i, j = (k + 1) // m, (k + 1) % m
            suffix[k] = suffix[k + 1] * grid[i][j] % MOD

        # calculate the product
        p = [[1] * m for _ in range(n)]

        for k in range(total):
            #  p[k] = prefix[k] * suffix[k]
            i, j = k // m, k % m
            p[i][j] = prefix[k] * suffix[k] % MOD
        
        return p
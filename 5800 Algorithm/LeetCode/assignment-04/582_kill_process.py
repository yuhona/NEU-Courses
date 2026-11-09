
from collections import defaultdict


class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        '''
        To Do:
            return a list, ID of process that will be killed, in any order
        Input:    
            pid = [1, 3, 10, 5]
            ppid = [3, 0, 5, 3]
        
        Approach 1: Recurssive DFS
        Step1: Build an adjancency list
            parent_to_children:
            3 :[1, 5]
            5 : [10]

        Step2: recurssively visit the kill and its children

        Approach 2: Iterative DFS 
        '''

        n = len(pid)

        parent_to_children  = {}

        for i in range(n):
            if ppid[i] not in parent_to_children:
                parent_to_children[ppid[i]] = []
                
            parent_to_children[ppid[i]].append(pid[i])

        # def dfs(curr):
        #     result.append(curr)

        #     for child in parent_to_children.get(curr, []):
        #         dfs(child)

        #     return 
        
        # result = []
        # dfs(kill)

        stack = [kill]
        result = []

        while stack:
            curr = stack.pop()
            result.append(curr)

            for child in parent_to_children.get(curr, []):
                stack.append(child)
            
        return result


      



# =====================================
# Test Cases
# =====================================

if __name__ == "__main__":
    sol = Solution()

    # Test 1: Kill a process with one child
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5

    result = sol.killProcess(pid, ppid, kill)
    print("Test 1:", result)
    assert set(result) == {5, 10}

    # Test 2: Kill the root process
    kill = 3

    result = sol.killProcess(pid, ppid, kill)
    print("Test 2:", result)
    assert set(result) == {1, 3, 5, 10}

    # Test 3: Kill a leaf process
    kill = 1

    result = sol.killProcess(pid, ppid, kill)
    print("Test 3:", result)
    assert set(result) == {1}

    # Test 4: Single process
    pid = [1]
    ppid = [0]
    kill = 1

    result = sol.killProcess(pid, ppid, kill)
    print("Test 4:", result)
    assert set(result) == {1}

    print("\nAll tests passed!")

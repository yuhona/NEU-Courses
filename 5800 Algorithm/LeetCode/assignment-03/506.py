class Solution:
    '''
    1. store the tuple (score, idx)
    [10,3,8,9,4]
    2. sort the score
    [(10, 0), (9, 3), (8, 2), (4, 4), (3, 1)]
    3. give the rank
    idx: 0, 1, 2, 3, 4
    rank:1, 5, 3, 2, 4
    O(n logn)
    O(n)
    '''
    def findRelativeRanks(self, score: list[int]) -> list[str]:        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            arr_left = merge_sort(arr[:mid])
            arr_right = merge_sort(arr[mid:])

            return merge(arr_left, arr_right)

        def merge(L1, L2): # new list of sorted 
            rank = []
            i, j = 0, 0
            # L1: [(10, 0), (3, 1)] L2:[((9, 3), (8, 2), (4, 4))]
            #       i.                    j
            #.               i.           j
            #                i.                   j
            while i < len(L1) and j < len(L2):
                if L1[i][0] > L2[j][0]:
                    rank.append(L1[i])
                    i += 1
                else:
                    rank.append(L2[j])
                    j += 1
            
            if i < len(L1):
                rank += L1[i:]
            if j < len(L2):
                rank += L2[j:]
            
            return rank

        score_idx = [(score[i], i) for i in range(len(score))]

        ranked_score_idx = merge_sort(score_idx)

        ans = [""] * len(score)

        for i in range(len(ranked_score_idx)):
            idx = ranked_score_idx[i][1]
            if i == 0:
                ans[idx] = "Gold Medal"
            elif i == 1:
                ans[idx] = "Silver Medal"
            elif i == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(i + 1)

        return ans


        
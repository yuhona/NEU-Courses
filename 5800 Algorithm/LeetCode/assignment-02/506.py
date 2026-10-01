class Solution:
    '''
    1. store the (score, idx) in rank
    2. sort the rank in decreasing order, by score
    3. store the rank of the ith athlete:
    score = [10, 3,    8,    9,  4]
             1st 5th   3rd   2nd 4th
    rank = [(10,0), (3,1), (8,2), (9,3),(4,4)]
           [(10,0), (9,3),(8,2), (4,4),(3,1)]
    res[0] = [Glod]
    res[3] = [Siler]
    res[2] = [Bronze]
    res[4] = [4th]
    res[1] = [5th]
    res[] = [Glod, 5, Bronze, Siler, 4]
    store the rank of the ith athlete:
        enumerate the rank from 0 to n - 1 as i:
            score, idx = rank[i]
            res[idx] = i
    '''
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        rank = []
        for i in range (len(score)):
            rank.append((score[i], i))
        
        rank.sort(reverse=True)

        res = [""] * len(score)

        for i in range(len(rank)):
            score, idx = rank[i]
            if i == 0:
                res[idx] = "Gold Medal"
            elif i == 1:
                res[idx] = "Silver Medal"
            elif i == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(i + 1)
                
        return res
            
class Solution:
    '''
    1. count all the characters, use a dic [char: cnt]
    2. sort the pair(cnt, char) in decreasing order
    3. append the string : char * cnt
    '''
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        freq_to_char = []
        for c, cnt in freq.items():
            freq_to_char.append((cnt, c))
        
        freq_to_char.sort(reverse = True)#O(k log k)

        res = ""
        for cnt, c in freq_to_char:
            res += c * cnt

        return res
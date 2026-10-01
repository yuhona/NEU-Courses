class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        '''
        return the k most frequent, odered by frequency and lexicographic
        1. count the word by frequency, use dict {word: frequency}
        2. restore the (frequency, word) in a list
        sort(-frequency, word)
        '''
        freq_words = {}
        for word in words:
            freq_words[word] = freq_words.get(word, 0) + 1
        
        freq = []
        for word, cnt in freq_words.items():
            freq.append((-cnt, word))

        freq.sort()

        return [word for cnt, word in freq[:k]]
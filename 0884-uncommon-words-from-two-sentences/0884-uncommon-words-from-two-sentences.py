class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_word = s1.split()
        s2_word = s2.split()
        all_words = s1_word + s2_word
        freq = {}
        for word in all_words:
            freq[word] = freq.get(word,0) + 1
        return [word for word in freq if freq[word] == 1]
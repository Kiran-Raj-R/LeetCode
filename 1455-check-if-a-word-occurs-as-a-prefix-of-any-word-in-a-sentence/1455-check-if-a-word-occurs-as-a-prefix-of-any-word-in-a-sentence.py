class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        n = len(searchWord)
        # for i in range(len(words)):
        #     if searchWord in words[i][0:n]:
        for i,word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1
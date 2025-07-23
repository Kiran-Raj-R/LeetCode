class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length = [len(i.split(' ')) for i in sentences]
        return max(length)
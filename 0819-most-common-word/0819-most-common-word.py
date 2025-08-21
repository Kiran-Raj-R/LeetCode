class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?,;'.":
            paragraph = paragraph.replace(c," ")
        freq = {}
        res = ""
        count = 0
        for word in paragraph.lower().split():
            if word in banned:
                continue
            elif word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
            if freq[word] > count:
                count = freq[word]
                res = word
        return res
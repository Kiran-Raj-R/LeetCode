class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # freq = Counter(words[0])
        # for word in words:
        #     freq &= Counter(word)
        # return list(freq.elements())
        common = list(words[0])
        for word in words[1:]:
            new_common = []
            for ch in word:
                if ch in common:
                    new_common.append(ch)
                    common.remove(ch)
            common = new_common
        return common
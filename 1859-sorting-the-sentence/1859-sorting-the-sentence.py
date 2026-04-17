class Solution:
    def sortSentence(self, s: str) -> str:
        # words = s.split()
        # result = [""] * len(words)

        # for word in words:
        #     position = int(word[-1]) - 1
        #     result[position] = word[:-1]

        # return " ".join(result)   
        words = [''] * 9
        sParsed = s.split()          

        for word in sParsed:
            j = ord(word[-1]) - 49
            words[j] = word[:-1]

        return " ".join(words).rstrip() 
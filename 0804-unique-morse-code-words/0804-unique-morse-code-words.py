class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
        ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            s = ''
            for w in word:
                s += code[ord(w) - 97]
            res.add(s)
        return len(res)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = c = 0
        s = Counter(secret)
        g = Counter(guess)
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                b += 1
                s[guess[i]] -= 1
                g[guess[i]] -= 1
        for j in g:
            if g[j] > 0 and j in s and s[j] > 0:
                c += min(g[j], s[j])
        return str(b) + 'A' + str(c) + 'B'
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # b = c = 0
        # s = Counter(secret)
        # g = Counter(guess)
        # for i in range(len(guess)):
        #     if secret[i] == guess[i]:
        #         b += 1
        #         s[guess[i]] -= 1
        #         g[guess[i]] -= 1
        # for j in g:
        #     if g[j] > 0 and j in s and s[j] > 0:
        #         c += min(g[j], s[j])
        # return str(b) + 'A' + str(c) + 'B'
        b, c = 0, 0
        count = [0] * 10
        for s,g in zip(secret,guess):
            if s == g:
                b += 1
            else:
                s_num = ord(s) - ord('0')
                g_num = ord(g) - ord('0')
                if count[s_num] < 0: 
                    c += 1
                if count[g_num] > 0:
                    c += 1
                count[s_num] += 1
                count[g_num] -= 1
        return f'{b}A{c}B'
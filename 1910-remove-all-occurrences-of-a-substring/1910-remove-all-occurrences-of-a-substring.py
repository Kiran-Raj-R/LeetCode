class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = []
        length = len(part)
        end = part[-1]
        for ch in s:
            result.append(ch)
            if ch == end and len(result) >= length:
                if "".join(result[-length:]) == part:
                    del result[-length:]
        return "".join(result)
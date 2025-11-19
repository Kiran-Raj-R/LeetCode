class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        seen = set()
        for i, ch in enumerate(password):
            if i > 0 and ch == password[i-1]:
                return False
            if ch.isupper():
                seen.add('u')
            elif ch.islower():
                seen.add('l')
            elif ch.isdigit():
                seen.add('d')
            else:
                seen.add('s')
        return len(password) > 7 and len(seen) == 4
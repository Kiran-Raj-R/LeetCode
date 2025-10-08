class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        # b = ""
        # for i in range(len(command)):
        #     if command[i] == '(' and command[i + 1] == ')':
        #         res += 'o'
        #     elif command[i] == '(':
        #         b += '(' 
        #     elif command[i] == ')':
        #         b += ')'
        #     else:
        #         res += command[i]
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
                i += 1
            elif command[i:i+2] == '()':
                res += 'o'
                i += 2
            elif command[i:i+4] == '(al)':
                res += 'al'
                i += 4 
        return res
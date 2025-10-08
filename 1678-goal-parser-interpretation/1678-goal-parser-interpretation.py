class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        b = ""
        for i in range(len(command)):
            if command[i] == '(' and command[i + 1] == ')':
                res += 'o'
            elif command[i] == '(':
                b += '(' 
            elif command[i] == ')':
                b += ')'
            else:
                res += command[i]
        return res
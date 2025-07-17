class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # moves = list(moves)
        # origin = [0,0]
        # for move in moves:
        #     if move == 'R':
        #         origin[0] += 1
        #     elif move == 'L':
        #         origin[0] -= 1
        #     elif move == 'U':
        #         origin[1] += 1
        #     else:
        #         origin[1] -= 1
        
        # return origin == [0,0]

        return (moves.count("R") == moves.count("L")) and (moves.count("U") == moves.count("D"))
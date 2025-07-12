class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        can = capacity
        for i,x in enumerate(plants):
            if can < x:
                res += 2 * i
                can = capacity
            res += 1
            can -= x
        return res
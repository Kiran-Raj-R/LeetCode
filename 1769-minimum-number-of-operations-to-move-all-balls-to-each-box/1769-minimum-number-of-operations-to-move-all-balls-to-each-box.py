class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            c = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    c += abs(j - i)
            res.append(c)
        return res
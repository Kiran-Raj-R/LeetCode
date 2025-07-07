class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        bucket = defaultdict(list)

        for ids,size in enumerate(groupSizes):
            bucket[size].append(ids)

            if len(bucket[size]) == size:
                res.append(bucket.pop(size))
                # bucket[size] = []

        return res
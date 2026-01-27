class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = len(names)
        height_map = dict(zip(heights,names))
        sorted_height = sorted(heights,reverse=True)
        sorted_names = [height_map[h] for h in sorted_height]
        return sorted_names
class Solution:
    def average(self, salary: List[int]) -> float:
        sum1 = sum(salary)
        # for s in salary:
        #     sum1 += s
        return (sum1 - max(salary) - min(salary)) / (len(salary)-2)
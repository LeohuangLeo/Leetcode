class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        lis = [a!=b for a, b in zip(heights_sorted, heights)]
        return sum(lis)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i + 1]) for i, _ in enumerate(nums)]
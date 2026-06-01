class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums)
        for item in nums:
            ans.append(item)
        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest_length = 0
        current_length = 1

        uniques = set(nums)
        for num in uniques:
            temp = num
            while temp + 1 in uniques:
                temp += 1
                current_length += 1
            if current_length > longest_length:
                longest_length = current_length
            current_length = 1
        
        return longest_length
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = []
        frequency = []
        out = []
        if not nums:
            return []
        while nums:
            current_num = nums[0]
            unique_nums.append(current_num)
            frequency.append(nums.count(current_num))
            for i in range(nums.count(current_num)):
                nums.remove(current_num)
        
        for j in range(k):
            most_frequent_index = frequency.index(max(frequency))
            out.append(unique_nums[most_frequent_index])
            unique_nums.pop(most_frequent_index)
            frequency.pop(most_frequent_index)
        
        return out
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        for x in numbers:
            index1 += 1
            if (target - x) in numbers:
                return [index1, numbers.index(target - x) + 1] 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        product = numbers[index1] + numbers[index2]
        while product != target:
            if product > target:
                index2 -= 1
            else:
                index1 += 1
            product = numbers[index1] + numbers[index2]
        return [index1 + 1, index2 + 1]
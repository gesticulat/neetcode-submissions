class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            product = 1
            temp = nums[:]
            temp.remove(nums[i])
            for num in temp:
                product *= num
            out.append(product)
        return out
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for x in range(len(nums))]

        #find prefixes
        for i in range(len(nums)-1):
            for x in nums[:i+1]:
                out[i+1] *= x

        #multiply postfixes
        for i in range(-1, -1 * len(nums), -1):
            for x in nums[i:]:
                out[i-1] *= x

        return out
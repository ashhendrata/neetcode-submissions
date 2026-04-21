class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        prefix[0] = 1
        prefix[1] = nums[0]
        for i in range(2, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        print(prefix)

        suffix = [1] * len(nums)
        suffix[-1] = 1
        suffix[-2] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        print(suffix)

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res


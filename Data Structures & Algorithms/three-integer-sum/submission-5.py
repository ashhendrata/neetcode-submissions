class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) != 0:
                return []
            else:
                return [nums]

        nums.sort()
        # print(sorted_nums) # [-4, -1, -1, 0, 1, 2]

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right and left >= i and right <= len(nums) - 1:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                    continue
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                    continue
                if nums[left] + nums[right] == -nums[i]:
                    res.append([nums[left], nums[right], nums[i]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
        
        return res

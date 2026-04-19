class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies_map = {} # key = num, value = index
        counter = 0
        for num in nums:
            if num not in indicies_map:
                indicies_map[num] = counter
            if target - num in indicies_map and indicies_map[target - num] != counter:
                return [indicies_map[target - num], counter]
            counter += 1
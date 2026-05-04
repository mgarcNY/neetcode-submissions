class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for index, val in enumerate(nums):
            difference = target - val
            if difference in sol:
                return [sol[difference],index]
            sol[val] = index            
                
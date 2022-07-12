class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Liste = dict()
        for i,n in enumerate(nums):
            diff = target - nums[i]
            if diff in Liste:
                return [Liste[diff], i]
            Liste[n] = i
        return None
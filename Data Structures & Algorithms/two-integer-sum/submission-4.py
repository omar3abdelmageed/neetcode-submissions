class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for i in range(len(nums)):

            compliment = target - nums[i]

            for j in range(len(nums)):

                if nums[j] == compliment and j != i:

                    return [i,j]

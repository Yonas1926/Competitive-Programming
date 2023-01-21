class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0] * len(nums)
        for i in range(len(nums)):
            for j in nums:
                if nums[i] == j:
                    continue
                elif j < nums[i]:
                    counter[i] += 1 
        return counter
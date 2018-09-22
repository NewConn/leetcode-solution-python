class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = len(nums)
        for i in range(count):
            for j in range(i + 1, count):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
class Solution:
    def twoSum(self, nums, target):
        """
        :param nums: array
        :param target: target
        :return: indices
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
class Solution:
    def twoSum(self, nums, target):
        """
        wrong solution
        :param nums: array
        :param target: target
        :return: indices
        """
        map = {}
        for i in range(len(nums)):
            if not nums[i] in map:
                map[target - nums[i]] = i
            else:
                return [map[nums[i]], i]


s = Solution()
nums = [2, 7, 11, 15]
target = 18
print(s.twoSum(nums, target))

nums = [3, 3]
target = 6
print(s.twoSum(nums, target))

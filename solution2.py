class Solution:
    def twoSum(self, nums, target):
        """
        wrong solution
        :param nums: array
        :param target: target
        :return: indices
        """
        map = {}
        for i in nums:
            if not i in map:
                map[target - i] = i
            else:
                return [nums.index(map[i]), nums.index(i)]


s = Solution()
nums = [2, 7, 11, 15]
target = 18
print(s.twoSum(nums, target))

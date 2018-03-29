# Two Sum

## 题目描述

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## 样例

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

## 解题思路

### 解法一

非常常规的暴力破解法，分两次循环遍历数组，然后看看两个索引位置数字的加和是否等于目标数字。

如代码 solution1.py：

```python
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
```

### 解法二

由于暴力破解法的时间复杂度是O(n2)，要简化，比如计算一次，就用一个字典保存下来另一个需要加和需要的数字，
继续遍历，这样如果一旦遍历遇到了另一个数字，那么就代表两次能够累加得到目标数字，然后将二者的索引返回即可。

所以我们可能会用字典来保存两个加和需要的数字，字典键名是另一个需要的数字，键值是当前数字。

如代码 solution2.py：

```python
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
```

但这样其实会导致一个问题，就是当数组两个数字的相同的条件下，返回的索引是相同的，如
nums = [3, 3]，target = 6，这样就会返回 [0, 0]，所以这种解法是不行的。

所以我们需要保存索引位置，键名是另一个需要的数字，键值是索引位置，如 solution3.py 所示：

```python
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
```

这样时间复杂度就变成了 O(n)，效率大大提高。